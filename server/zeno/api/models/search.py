# from enum import StrEnum
from uuid import UUID

from sqlalchemy import (
    String,
    ForeignKey
    )
from sqlalchemy.orm import (Mapped,
                            mapped_column,
                            relationship
                            )



class SearchHistory(RecordModel):
    __tablename__ = "searchHistory"

    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    user = relationship("user", back_populates="searchHistory")

    query: Mapped[str] = mapped_column(String(256))


