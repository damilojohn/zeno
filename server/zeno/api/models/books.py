from uuid import UUID
from typing import Optional
from datetime import datetime

from sqlalchemy import String, ForeignKey, Text, Integer, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import ARRAY

from zeno.api.models.base import RecordModel


class Book(RecordModel):
    __tablename__ = "books"

    title: Mapped[str] = mapped_column(String(512), nullable=False, index=True)
    author: Mapped[str] = mapped_column(String(256), nullable=False, index=True)
    isbn: Mapped[Optional[str]] = mapped_column(
        String(13), nullable=True, unique=True, index=True
    )
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    goodreads_id: Mapped[Optional[str]] = mapped_column(
        String(64), nullable=True, index=True
    )
    amazon_id: Mapped[Optional[str]] = mapped_column(
        String(64), nullable=True, index=True
    )
    cover_image_url: Mapped[Optional[str]] = mapped_column(String(1024), nullable=True)
    publication_year: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    page_count: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    genres: Mapped[Optional[list[str]]] = mapped_column(ARRAY(String), nullable=True)

    recommendations = relationship(
        "BookRecommendation",
        back_populates="book",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    reading_history = relationship(
        "ReadingHistory",
        back_populates="book",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )


class ReadingHistory(RecordModel):
    __tablename__ = "reading_history"

    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    book_id: Mapped[UUID] = mapped_column(
        ForeignKey("books.id", ondelete="CASCADE"), nullable=False, index=True
    )
    read_at: Mapped[Optional[datetime]] = mapped_column(
        TIMESTAMP(timezone=True), nullable=True
    )
    rating: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)

    user = relationship("User", back_populates="reading_history")
    book = relationship("Book", back_populates="reading_history")
