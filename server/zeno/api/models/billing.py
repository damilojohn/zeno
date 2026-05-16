from enum import StrEnum
from datetime import datetime
from uuid import UUID

from sqlalchemy import String, TIMESTAMP, ForeignKey, Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from zeno.api.models.base import RecordModel


class Plan(StrEnum):
    free = "free"
    pro = "pro"


class SubscriptionStatus(StrEnum):
    active = "active"
    trialing = "trialing"
    past_due = "past_due"
    cancelled = "cancelled"


class Subscription(RecordModel):
    __tablename__ = "subscriptions"

    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
        unique=True,
    )
    stripe_customer_id: Mapped[str] = mapped_column(
        String(64), nullable=False, unique=True, index=True
    )
    stripe_subscription_id: Mapped[str] = mapped_column(
        String(64), nullable=True, unique=True, index=True
    )
    plan: Mapped[Plan] = mapped_column(
        SAEnum(Plan, name="plan"), nullable=False, default=Plan.free
    )
    status: Mapped[SubscriptionStatus] = mapped_column(
        SAEnum(SubscriptionStatus, name="subscriptionstatus"),
        nullable=False,
        default=SubscriptionStatus.active,
    )
    current_period_end: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), nullable=True
    )

    user = relationship("User", back_populates="subscription")
