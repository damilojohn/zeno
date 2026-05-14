from enum import StrEnum
from typing import Optional
from uuid import UUID

from sqlalchemy import String, ForeignKey, Text, Integer, Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from zeno.api.models.base import RecordModel


class JobStatus(StrEnum):
    pending = "pending"
    running = "running"
    complete = "complete"
    failed = "failed"


class SearchJob(RecordModel):
    __tablename__ = "search_jobs"

    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    query: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[JobStatus] = mapped_column(
        SAEnum(JobStatus, name="jobstatus"), nullable=False, default=JobStatus.pending
    )
    error_message: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    user = relationship("User", back_populates="search_jobs")
    recommendations = relationship(
        "BookRecommendation", back_populates="search_job",
        cascade="all, delete-orphan", passive_deletes=True,
    )


class BookRecommendation(RecordModel):
    __tablename__ = "book_recommendations"

    search_job_id: Mapped[UUID] = mapped_column(
        ForeignKey("search_jobs.id", ondelete="CASCADE"), nullable=False, index=True
    )
    book_id: Mapped[UUID] = mapped_column(
        ForeignKey("books.id", ondelete="CASCADE"), nullable=False, index=True
    )
    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    relevance_score: Mapped[Optional[float]] = mapped_column(nullable=True)
    recommendation_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    search_job = relationship("SearchJob", back_populates="recommendations")
    book = relationship("Book", back_populates="recommendations")
    user = relationship("User", back_populates="book_recommendations")


class UserInterest(RecordModel):
    __tablename__ = "user_interests"

    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    topic: Mapped[str] = mapped_column(String(256), nullable=False, index=True)
    weight: Mapped[float] = mapped_column(nullable=False, default=1.0)

    user = relationship("User", back_populates="interests")


class TopicRecommendation(RecordModel):
    __tablename__ = "topic_recommendations"

    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    topic: Mapped[str] = mapped_column(String(256), nullable=False, index=True)
    score: Mapped[float] = mapped_column(nullable=False, default=0.0)

    user = relationship("User", back_populates="topic_recommendations")
