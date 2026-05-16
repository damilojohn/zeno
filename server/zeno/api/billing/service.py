"""
Stripe billing service.

Flow:
  1. User hits POST /billing/checkout
       → create (or retrieve) a Stripe Customer for this user
       → create a Stripe Checkout Session for the chosen price
       → return the session URL; frontend redirects user there

  2. User completes payment on Stripe's hosted page
       → Stripe fires `checkout.session.completed` webhook

  3. POST /billing/webhook receives the event
       → verify the signature (STRIPE_WEBHOOK_SECRET)
       → handle the event type and update the Subscription row in DB

  4. User hits POST /billing/portal
       → create a Stripe Billing Portal session
       → return the URL; frontend redirects user there
       → user can upgrade, downgrade, or cancel from Stripe's hosted portal
"""

import stripe
from sqlalchemy.ext.asyncio import AsyncSession

from zeno.api.core.config import Settings

settings = Settings()
stripe.api_key = settings.stripe_secret_key


async def create_checkout_session(
    price_id: str, user_id: str, user_email: str, db: AsyncSession
) -> str:
    """
    Creates a Stripe Checkout session and returns the URL.

    Steps:
      1. Look up or create a Stripe Customer for this user
      2. Call stripe.checkout.Session.create() with the price_id
      3. Return session.url
    """
    # TODO: implement
    raise NotImplementedError


async def create_portal_session(user_id: str, db: AsyncSession) -> str:
    """
    Creates a Stripe Customer Portal session and returns the URL.

    Steps:
      1. Fetch the user's stripe_customer_id from the Subscription table
      2. Call stripe.billing_portal.Session.create()
      3. Return session.url
    """
    # TODO: implement
    raise NotImplementedError


async def handle_webhook(
    payload: bytes, stripe_signature: str, db: AsyncSession
) -> None:
    """
    Verifies and processes a Stripe webhook event.

    Events to handle:
      - checkout.session.completed   → create/update Subscription row, set plan=pro, status=active
      - customer.subscription.updated → update plan/status/current_period_end
      - customer.subscription.deleted → set status=cancelled
      - invoice.payment_failed        → set status=past_due, (optionally email user)

    Steps:
      1. stripe.Webhook.construct_event(payload, stripe_signature, settings.stripe_webhook_secret)
         — raises stripe.error.SignatureVerificationError if invalid; let it propagate as 400
      2. Switch on event["type"] and call the appropriate handler
    """
    # TODO: implement
    raise NotImplementedError


async def get_subscription(user_id: str, db: AsyncSession):
    """Fetch the user's current Subscription row from DB."""
    # TODO: implement
    raise NotImplementedError
