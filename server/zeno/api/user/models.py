from enum import StrEnum
from uuid import UUID

from sqlalchemy import (
    Boolean,
    Integer,
    String,
    ForeignKey
    )
from sqlalchemy.orm import (Mapped,
                            mapped_column,
                            relationship
                            )


from zeno.api.core.base_schemas import RecordModel


class OauthProvider(StrEnum):
    google = "google"
    apple = "apple"


class User(RecordModel):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String(320),
                                       nullable=False,
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
    searches = relationship("SearchHistory", back_populates="user")
    favorite_books = relationship("FavoriteBook", back_populates="user")
    reading_lists = relationship("ReadingList", back_populates="user")


class SearchHistory(RecordModel):
    __tablename__ = "search_history"

    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    user = relationship("user", back_populates="search_history")

    query: Mapped[str] = mapped_column(String(256))
