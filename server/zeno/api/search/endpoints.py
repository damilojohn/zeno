from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from zeno.api.core.db import get_async_db_session
from zeno.api.core.responses import ApiResponse
from zeno.api.user.service import get_current_user
from zeno.api.user.schemas import UserResponse
from zeno.api.search.schemas import (
    SearchRequest,
    SearchJobResponse,
    SearchResultResponse,
)
from zeno.api.search.service import enqueue_search, get_job, get_search_history

router = APIRouter(prefix="/api/v2/search", tags=["search"])


@router.post(
    "/",
    response_model=ApiResponse[SearchJobResponse],
    status_code=status.HTTP_202_ACCEPTED,
)
async def create_search(
    request: SearchRequest,
    user: UserResponse = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db_session),
):
    job = await enqueue_search(request.query, user.id, db)
    return ApiResponse(
        msg="Search job created",
        data=SearchJobResponse.model_validate(job),
    )


# /history must be defined before /{job_id} so FastAPI doesn't try to parse
# "history" as a UUID
@router.get("/history", response_model=ApiResponse[list[SearchResultResponse]])
async def search_history(
    user: UserResponse = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db_session),
):
    jobs = await get_search_history(user.id, db)
    return ApiResponse(data=[SearchResultResponse.model_validate(j) for j in jobs])


@router.get("/{job_id}", response_model=ApiResponse[SearchResultResponse])
async def poll_job(
    job_id: UUID,
    user: UserResponse = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db_session),
):
    job = await get_job(job_id, user.id, db)
    return ApiResponse(data=SearchResultResponse.model_validate(job))
