from enum import StrEnum
from datetime import datetime

from sqlalchemy import Boolean, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from zeno.api.models.base import RecordModel, current_time, UUID


class OauthProvider(StrEnum):
    google = "google"
    apple = "apple"


class User(RecordModel):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(
        String(320), nullable=False, index=True, unique=True
    )
    email_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    full_name: Mapped[str] = mapped_column(String(128), unique=True, nullable=True)
    hashed_password: Mapped[str] = mapped_column(String(256), nullable=True)

    reset_tokens = relationship(
        "ResetTokens",
        back_populates="user",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    search_jobs = relationship(
        "SearchJob",
        back_populates="user",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    book_recommendations = relationship(
        "BookRecommendation",
        back_populates="user",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    reading_history = relationship(
        "ReadingHistory",
        back_populates="user",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    interests = relationship(
        "UserInterest",
        back_populates="user",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    topic_recommendations = relationship(
        "TopicRecommendation",
        back_populates="user",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    subscription = relationship(
        "Subscription",
        back_populates="user",
        cascade="all, delete-orphan",
        passive_deletes=True,
        uselist=False,  # one-to-one
    )


class ResetTokens(RecordModel):
    __tablename__ = "PasswordResetTokens"

    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    token_hash: Mapped[str] = mapped_column(String(64))
    to_expire: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
        default=current_time,
    )
    user = relationship("User", back_populates="reset_tokens")
