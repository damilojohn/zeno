"""
Base SQS worker. Handles the poll loop, graceful shutdown, and message lifecycle.
Subclasses implement process_message() with job-specific logic.
"""

import asyncio
import json
import signal
from abc import ABC, abstractmethod

import boto3
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from zeno.api.core.config import Settings
from zeno.api.core.utils import LOG

settings = Settings()


class SQSWorker(ABC):
    queue_url: str = settings.search_queue_url

    def __init__(self) -> None:
        self._shutdown = False
        self._engine = create_async_engine(settings.database_url)
        self.session_maker = async_sessionmaker(self._engine, expire_on_commit=False)
        self._sqs = boto3.client(
            "sqs",
            region_name=settings.aws_region,
            aws_access_key_id=settings.aws_access_key_id,
            aws_secret_access_key=settings.aws_secret_key,
        )

    @abstractmethod
    async def process_message(self, body: dict, db: AsyncSession) -> None:
        """Handle one decoded message. Raise on unrecoverable failure."""

    async def run(self) -> None:
        signal.signal(signal.SIGTERM, self._handle_sigterm)
        LOG.info("worker_started", queue=self.queue_url, worker=type(self).__name__)

        while not self._shutdown:
            await self._poll_once()

        await self._engine.dispose()
        LOG.info("worker_stopped", worker=type(self).__name__)

    async def _poll_once(self) -> None:
        try:
            response = await asyncio.to_thread(
                self._sqs.receive_message,
                QueueUrl=self.queue_url,
                WaitTimeSeconds=20,
                MaxNumberOfMessages=5,
                AttributeNames=["All"],
            )
        except Exception as e:
            LOG.error("sqs_receive_error", error=str(e))
            await asyncio.sleep(5)
            return

        messages = response.get("Messages", [])
        if messages:
            await asyncio.gather(*[self._handle_message(m) for m in messages])

    async def _handle_message(self, message: dict) -> None:
        receipt = message["ReceiptHandle"]

        try:
            body = json.loads(message["Body"])
        except (json.JSONDecodeError, KeyError) as e:
            LOG.error("malformed_sqs_message", error=str(e))
            # Malformed messages won't fix themselves — delete immediately
            await self._delete(receipt)
            return

        try:
            async with self.session_maker() as db:
                await self.process_message(body, db)
            await self._delete(receipt)
        except Exception as e:
            LOG.error("message_processing_failed", error=str(e), body=body)
            # Leave message in queue — SQS retries after visibility timeout,
            # then routes to DLQ after max receive count is reached.

    async def _delete(self, receipt: str) -> None:
        await asyncio.to_thread(
            self._sqs.delete_message,
            QueueUrl=self.queue_url,
            ReceiptHandle=receipt,
        )

    def _handle_sigterm(self, *_) -> None:
        LOG.info("sigterm_received", worker=type(self).__name__)
        self._shutdown = True
