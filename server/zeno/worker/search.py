from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from zeno.api.core.utils import LOG
from zeno.api.models import SearchJob
from zeno.api.models.search import JobStatus
from zeno.worker.base import SQSWorker


class SearchWorker(SQSWorker):
    async def process_message(self, body: dict, db: AsyncSession) -> None:
        job_id = UUID(body["job_id"])
        user_id = UUID(body["user_id"])
        query: str = body["query"]

        job = await self._get_job(job_id, db)
        if not job:
            LOG.warning("job_not_found", job_id=str(job_id))
            return

        job.status = JobStatus.running
        await db.commit()

        try:
            await self._run_agent(job, user_id, query, db)
        except Exception as e:
            job.status = JobStatus.failed
            job.error_message = str(e)
            await db.commit()
            LOG.error("agent_failed", job_id=str(job_id), error=str(e))
            raise  # propagate so base class leaves message for DLQ retry

    async def _run_agent(self, job: SearchJob, user_id: UUID, query: str, db: AsyncSession) -> None:
        # TODO: replace with agent harness
        # from zeno.api.search.agent.harness import run_agent
        # await run_agent(job, user_id, query, db)

        job.status = JobStatus.complete
        await db.commit()
        LOG.info("job_complete", job_id=str(job.id))

    @staticmethod
    async def _get_job(job_id: UUID, db: AsyncSession) -> SearchJob | None:
        result = await db.execute(select(SearchJob).where(SearchJob.id == job_id))
        return result.scalar_one_or_none()
