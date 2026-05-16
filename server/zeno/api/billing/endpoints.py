from fastapi import APIRouter, Depends, Request, status
from sqlalchemy.ext.asyncio import AsyncSession

from zeno.api.core.db import get_async_db_session
from zeno.api.core.responses import ApiResponse
from zeno.api.core.exceptions import BadRequestError
from zeno.api.user.service import get_current_user
from zeno.api.user.schemas import UserResponse
from zeno.api.billing.schemas import (
    CheckoutRequest,
    CheckoutResponse,
    PortalResponse,
    SubscriptionResponse,
)
from zeno.api.billing import service

router = APIRouter(prefix="/v2/billing", tags=["billing"])


@router.get("/subscription", response_model=ApiResponse[SubscriptionResponse])
async def get_subscription(
    user: UserResponse = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db_session),
):
    result = await service.get_subscription(str(user.id), db)
    return ApiResponse(data=result)


@router.post("/checkout", response_model=ApiResponse[CheckoutResponse])
async def create_checkout(
    request: CheckoutRequest,
    user: UserResponse = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db_session),
):
    url = await service.create_checkout_session(
        request.price_id, str(user.id), str(user.email), db
    )
    return ApiResponse(
        msg="Checkout session created",
        data=CheckoutResponse(checkout_url=url),
    )


@router.post("/portal", response_model=ApiResponse[PortalResponse])
async def billing_portal(
    user: UserResponse = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db_session),
):
    url = await service.create_portal_session(str(user.id), db)
    return ApiResponse(
        msg="Portal session created",
        data=PortalResponse(portal_url=url),
    )


@router.post(
    "/webhook", response_model=ApiResponse[None], status_code=status.HTTP_200_OK
)
async def stripe_webhook(
    request: Request,
    db: AsyncSession = Depends(get_async_db_session),
):
    """
    Stripe calls this directly — excluded from JWT auth.
    Raw bytes body is required for signature verification.
    """
    payload = await request.body()
    stripe_signature = request.headers.get("stripe-signature", "")

    try:
        await service.handle_webhook(payload, stripe_signature, db)
    except ValueError:
        raise BadRequestError("Invalid webhook payload")

    return ApiResponse(msg="Webhook processed")
