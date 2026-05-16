from datetime import datetime, timezone, timedelta
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from google.oauth2 import id_token
from google.auth.transport import requests


from zeno.api.core.utils import LOG
from zeno.api.core.security import (
    get_password_hash,
    create_access_token,
    verify_access_token,
    create_reset_token,
    verify_refresh_token,
    get_token_hash,
    verify_password,
    create_refresh_token,
)
from zeno.api.core.exceptions import (
    AppException,
    UnauthorizedError,
    ConflictError,
    BadRequestError,
    InternalServerError,
)
from zeno.api.user.schemas import (
    UserResponse,
    UserCreate,
    RegisterResponse,
    TokenResponse,
    ResetTokenResponse,
    LoginRequest,
)

from zeno.api.models.users import User, ResetTokens
from zeno.api.core.db import get_async_db_session
from zeno.api.core.config import Settings

settings = Settings()

oauth2scheme = OAuth2PasswordBearer(tokenUrl="/v2/auth/form-login")


async def get_current_user(
    token: str = Depends(oauth2scheme),
    session: AsyncSession = Depends(get_async_db_session),
) -> UserResponse:
    """Get current db user from JWT"""
    try:
        user_id = verify_access_token(token)
    except Exception as e:
        LOG.error(f"failed with error {e}")
        raise UnauthorizedError("Invalid token") from e

    result = await session.execute(select(User).filter(User.id == user_id))
    user = result.scalar_one_or_none()
    if user:
        return UserResponse(email=user.email, is_verified=user.email_verified, id=user.id)
    raise UnauthorizedError("Invalid authentication credentials")


async def add_new_user(
    new_user: UserCreate, session: AsyncSession = Depends(get_async_db_session)
):
    try:
        result = await session.execute(
            select(User).filter(User.email == new_user.email)
        )
        existing_user = result.scalar_one_or_none()

        if existing_user:
            LOG.info("Tried to create already existing user... Failing with 409")
            raise ConflictError("User with this email already exists")

        hashed_pwd = get_password_hash(new_user.password)
        db_user = User(email=new_user.email, hashed_password=hashed_pwd)
        session.add(db_user)
        await session.commit()
        await session.refresh(db_user)

        access_token = create_access_token({"sub": str(db_user.id)})
        refresh_token = create_refresh_token({"sub": str(db_user.id)})

        return RegisterResponse(
            email=new_user.email,
            is_verified=False,
            access_token=access_token,
            refresh_token=refresh_token,
            message="User created successfully",
        )

    except AppException:
        raise
    except Exception as e:
        LOG.error("failed to create user", error=str(e))
        raise InternalServerError()


async def authenticate_user(
    user: LoginRequest, session: AsyncSession = Depends(get_async_db_session)
):
    try:
        result = await session.execute(select(User).filter(User.email == user.email))
        db_user = result.scalar_one_or_none()

        if not db_user or not verify_password(user.password, db_user.hashed_password):
            raise UnauthorizedError("Invalid username or password")

        access_token = create_access_token({"sub": str(db_user.id)})
        refresh_token = create_refresh_token({"sub": str(db_user.id)})

        return TokenResponse(
            access_token=access_token, refresh_token=refresh_token, token_type="bearer"
        )

    except AppException:
        raise
    except Exception as e:
        LOG.error("authentication failed", error=str(e))
        raise UnauthorizedError("Invalid username or password")


def get_refresh_token(token: str):
    try:
        user_id = verify_refresh_token(token)
        access_token = create_access_token({"sub": user_id})
        refresh_token = create_refresh_token({"sub": user_id})

        return TokenResponse(
            access_token=access_token, refresh_token=refresh_token, token_type="bearer"
        )
    except Exception as e:
        LOG.info(f"failed with error {e}")
        raise UnauthorizedError("Invalid token credentials")


async def send_reset_mail(token: str, email: str, username: str):
    """Generates password reset mail"""
    from zeno.api.core.email import send_password_reset_email

    email_sent = await send_password_reset_email(email, token, username)
    if not email_sent:
        LOG.info(f"Failed to send email, logging token instead: {token}")
    else:
        LOG.info(f"Password reset email sent successfully to {email}")


async def reset_password(email: str, db_session: AsyncSession):
    try:
        LOG.info("Fetching user ....")
        result = await db_session.execute(select(User).filter(User.email == email))
        db_user = result.scalar_one_or_none()

        if not db_user:
            return ResetTokenResponse(
                msg="Password reset email sent successfully"
            )

        token = create_reset_token()
        LOG.info(f"displaying token in logs for tests token : {token}")
        hashed_token = get_token_hash(token)
        db_token = ResetTokens(
            token_hash=hashed_token,
            user_id=db_user.id,
            to_expire=datetime.now(timezone.utc)
            + timedelta(minutes=settings.reset_tok_exp),
        )
        db_session.add(db_token)
        await db_session.commit()

    except AppException:
        raise
    except Exception as e:
        LOG.error("password reset failed", error=str(e))
        raise InternalServerError()

    return ResetTokenResponse(msg="Password reset email sent successfully")


async def create_new_password(new_password: str, token: str, db_session: AsyncSession):
    try:
        token_hash = get_token_hash(token)
        result = await db_session.execute(
            select(ResetTokens)
            .filter(ResetTokens.token_hash == token_hash)
            .order_by(ResetTokens.to_expire.desc())
        )
        db_result = result.scalar_one_or_none()

        if not db_result:
            LOG.info("DB Hash and token hash not equal")
            raise BadRequestError("Failed to verify reset token")

        to_expire = db_result.to_expire
        curr_time = datetime.now(timezone.utc)
        if curr_time > to_expire:
            LOG.info("Reset token expired..")
            raise BadRequestError("Reset token expired")

        new_password_hash = get_password_hash(new_password)
        try:
            result = await db_session.execute(
                select(User).filter_by(id=db_result.user_id)
            )
            db_user = result.scalar_one_or_none()
            if db_user:
                db_user.hashed_password = new_password_hash
                LOG.info("Password written to db")
                delete_result = await db_session.execute(
                    select(ResetTokens).filter(ResetTokens.user_id == db_user.id)
                )
                for token_to_delete in delete_result.scalars().all():
                    await db_session.delete(token_to_delete)
                await db_session.commit()
                return "Password changed successfully"
        except SQLAlchemyError as e:
            LOG.error("db write failed", error=str(e), exc_info=True)
            raise InternalServerError()

    except AppException:
        raise
    except Exception as e:
        LOG.error("failed to create new password", error=str(e))
        raise InternalServerError()


async def handle_google_oauth(
    code: str, redirect_uri: str, session: AsyncSession
):
    try:
        idinfo = id_token.verify_oauth2_token(
            code, requests.Request(), settings.google_client_id
        )

        if idinfo["iss"] not in ["accounts.google.com", "https://accounts.google.com"]:
            raise ValueError("Invalid issuer")

        email = idinfo["email"]
        name = idinfo.get("name", "")

        result = await session.execute(select(User).filter(User.email == email))
        user = result.scalar_one_or_none()

        if not user:
            user = User(
                email=email,
                username=name or email.split("@")[0],
                auth_provider="google",
                is_verified=True,
            )
            session.add(user)
            await session.commit()
            await session.refresh(user)

        access_token = create_access_token({"sub": str(user.id)})
        refresh_token = create_refresh_token({"sub": str(user.id)})

        from zeno.api.user.schemas import GoogleAuthResponse
        return GoogleAuthResponse(
            user=UserResponse(email=email, is_verified=True, id=user.id),
            access_token=access_token,
            refresh_token=refresh_token,
            message="Authenticated successfully",
        )

    except AppException:
        raise
    except SQLAlchemyError as e:
        await session.rollback()
        LOG.error("error handling google auth", error=str(e))
        raise InternalServerError("Error authenticating user")
