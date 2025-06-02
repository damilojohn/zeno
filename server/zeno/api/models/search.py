from enum import StrEnum
from uuid import UUID

from sqlalchemy import (
    String,
    ForeignKey
    )
from sqlalchemy.orm import (Mapped,
                            mapped_column,
                            relationship
                            )


from zeno.api.core.base_schemas import RecordModel


class SearchHistory(RecordModel):
    __tablename__ = "search_history"

    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    user = relationship("user", back_populates="search_history")

    query: Mapped[str] = mapped_column(String(256))