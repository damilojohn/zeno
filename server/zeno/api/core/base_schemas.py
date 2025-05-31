from datetime import datetime
from uuid import UUID

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import TIMESTAMP, Uuid, inspect


from zeno.api.core.utils import current_time, generate_uuid


class Model(DeclarativeBase):
    __abstract__ = True # sqlachemy doesn't create tables for these classes


class TimeStampedModel(Model):
    __abstract__ = True

    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False, index=True, default=current_time,
        index=True
        )

    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=True,
        default=None,
        index=True
        )

    def set_modified_at(self):
        self.modified_at = current_time()

    def set_deleted_at(self):
        self.deleted_at = current_time()


class RecordModel(TimeStampedModel):
    id: Mapped[UUID] = mapped_column(Uuid,
                                     primary_key=True,
                                     index=True,
                                     default=generate_uuid)

    def _repr__(self) -> str:
        insp = inspect(self)
        if insp.identity is not None:
            id_value = insp.identity[0]
            return f"{self.__class__.__name__}(id={id_value!r})"
        return f"{self.__class__.__name__}(id=None)"

    def __hash__(self) -> int:
        return self.id.int

    def __eq__(self, _value):
        return isinstance(_value, self.__class__) and self.id == _value.id
