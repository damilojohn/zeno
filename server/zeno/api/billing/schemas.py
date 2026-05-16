from pydantic import BaseModel
from zeno.api.models.billing import Plan, SubscriptionStatus


class CheckoutRequest(BaseModel):
    price_id: str  # Stripe Price ID (e.g. price_xxx) from your Stripe dashboard


class CheckoutResponse(BaseModel):
    checkout_url: str  # redirect the user here to complete payment


class PortalResponse(BaseModel):
    portal_url: str  # redirect the user here to manage their subscription


class SubscriptionResponse(BaseModel):
    plan: Plan
    status: SubscriptionStatus
    current_period_end: str | None = None

    model_config = {"from_attributes": True}
