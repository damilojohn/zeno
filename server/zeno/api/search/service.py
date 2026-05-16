import json
import asyncio
from uuid import UUID

from botocore.exceptions import BotoCoreError, ClientError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from zeno.api.core.config import Settings
from zeno.api.core.utils import LOG
from zeno.api.core.exceptions import NotFoundError
from zeno.api.models.search import SearchJob, JobStatus, BookRecommendation

settings = Settings()


async def enqueue_search(
    query: str, user_id: UUID, db: AsyncSession, sqs_client
) -> SearchJob:
    job = SearchJob(user_id=user_id, query=query, status=JobStatus.pending)
    db.add(job)
    await db.commit()
    await db.refresh(job)

    if settings.search_queue_url:
        try:
            await asyncio.to_thread(
                sqs_client.send_message,
                QueueUrl=settings.search_queue_url,
                MessageBody=json.dumps(
                    {
                        "job_id": str(job.id),
                        "user_id": str(user_id),
                        "query": query,
                    }
                ),
                MessageGroupId=str(user_id),
            )
        except (BotoCoreError, ClientError) as e:
            job.status = JobStatus.failed
            job.error_message = f"Failed to enqueue job: {e}"
            await db.commit()
            LOG.error("sqs_enqueue_failed", job_id=str(job.id), error=str(e))
    else:
        LOG.warning(
            "SQS_QUEUE_URL not set — job created but not queued", job_id=str(job.id)
        )

    return job


async def get_job(job_id: UUID, user_id: UUID, db: AsyncSession) -> SearchJob:
    result = await db.execute(
        select(SearchJob)
        .where(SearchJob.id == job_id, SearchJob.user_id == user_id)
        .options(
            selectinload(SearchJob.recommendations).selectinload(
                BookRecommendation.book
            )
        )
    )
    job = result.scalar_one_or_none()
    if not job:
        raise NotFoundError("Search job not found")
    return job


async def get_search_history(user_id: UUID, db: AsyncSession) -> list[SearchJob]:
    result = await db.execute(
        select(SearchJob)
        .where(SearchJob.user_id == user_id)
        .options(
            selectinload(SearchJob.recommendations).selectinload(
                BookRecommendation.book
            )
        )
        .order_by(SearchJob.created_at.desc())
    )
    return list(result.scalars().all())
