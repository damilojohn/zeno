from typing import Optional
from datetime import datetime
from pydantic import BaseModel, UUID4

from zeno.api.models.search import JobStatus


class SearchRequest(BaseModel):
    query: str


class SearchJobResponse(BaseModel):
    job_id: UUID4
    status: JobStatus
    query: str
    created_at: datetime

    model_config = {"from_attributes": True}


class BookResponse(BaseModel):
    id: UUID4
    title: str
    author: str
    isbn: Optional[str] = None
    description: Optional[str] = None
    cover_image_url: Optional[str] = None
    publication_year: Optional[int] = None
    genres: Optional[list[str]] = None

    model_config = {"from_attributes": True}


class RecommendationResponse(BaseModel):
    book: BookResponse
    relevance_score: Optional[float] = None
    recommendation_order: int

    model_config = {"from_attributes": True}


class SearchResultResponse(BaseModel):
    job_id: UUID4
    status: JobStatus
    query: str
    created_at: datetime
    error_message: Optional[str] = None
    recommendations: list[RecommendationResponse] = []

    model_config = {"from_attributes": True}
