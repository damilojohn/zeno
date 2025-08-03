from enum import StrEnum
from datetime import datetime

from sqlalchemy import (
    Boolean,
    String,
    TIMESTAMP,
    ForeignKey,
    Enum
    )

from sqlalchemy.orm import (Mapped,
                            mapped_column,
                            relationship,
                            )


from zeno.api.models.base import RecordModel, current_time, Uuid, UUID


class OauthProvider(StrEnum):
    google = "google"
    apple = "apple"


class User(RecordModel):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String(320),
                                       nullable=True,
                                       index=True,
                                       unique=True)
    email_verified: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )
    username: Mapped[str] = mapped_column(String(128))
    # password nullable for oauth users

    hashed_password: Mapped[str] = mapped_column(String(256),
                                                 nullable=True)
    reset_tokens = relationship("ResetTokens", back_populates="users")
    # oauth_provider: Mapped[OauthProvider] = mapped_column(Enum(enums=OauthProvider))

    # searches = relationship("SearchHistory", back_populates="user")
    # favorite_books = relationship("FavoriteBook", back_populates="user")
    # reading_lists = relationship("ReadingList", back_populates="user")


class ResetTokens(RecordModel):
    __tablename__ = "PasswordResetTokens"
    user_id: Mapped[UUID] = mapped_column(
                                        ForeignKey("users.id",
                                        ondelete="CASCADE"),
                                        nullable=False
    )
    token_hash: Mapped[str] = mapped_column(String(64))
    to_expire: Mapped[datetime] = mapped_column(TIMESTAMP(
            timezone=True),
            nullable=False,
            default=current_time,
    )
    users = relationship("User", back_populates="reset_tokens")
