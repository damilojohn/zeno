from enum import StrEnum

from sqlalchemy import (
    Boolean,
    String,
    )
from sqlalchemy.orm import (Mapped,
                            mapped_column,
                            relationship
                            )


from zeno.api.models.base import RecordModel


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