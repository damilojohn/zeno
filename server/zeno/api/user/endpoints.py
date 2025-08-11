from typing import Annotated
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.background import P
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from zeno.api.user.schemas import (
    UserResponse,
    UserCreate,
    UserResponse,
    LoginRequest,
    RegisterResponse,
    RefreshRequest,
    TokenResponse,
    ForgotPasswordRequest,
    PasswordResetRequest,
    PasswordResetResponse,
    ResetTokenResponse
)

from zeno.api.models.users import User
from zeno.api.core.db import get_db_session, get_async_db_session
from zeno.api.user.service import (
    get_current_user,
    add_new_user,
    authenticate_user,
    get_refresh_token,
    reset_password,
    create_new_password
)
from zeno.api.core.email import send_test_email

router = APIRouter(prefix="/v2/auth", tags=["users"])



@router.get("/me", response_model=UserResponse)
async def get_user_profile(
    user: UserResponse = Depends(get_current_user)
):
    """
    Get the current user's profile.
    """
    return user


@router.post(
    "/register",
    response_model=RegisterResponse,
    status_code=status.HTTP_201_CREATED
)
async def register_user(
    user: UserCreate,
    session: AsyncSession = Depends(get_async_db_session)
):
    """
    Register a new user with email and password.

    Args:
    user: UserCreate Object
    session: db_session

    Returns:
    RegisterResponse
    """
    try:
        new_user = await add_new_user(user, session)
        return new_user
    except Exception as e:
        raise e


@router.post("/login",
             response_model=TokenResponse,
             status_code=200)
async def login(
    login_data: LoginRequest,
    session: AsyncSession = Depends(get_async_db_session)
):
    """
    Login with email and password.

    Args:

    login_data: LoginRequest

    Returns:
    TokenResponse : access_token and refresh_token

    """
    return await authenticate_user(login_data, session)


@router.post("/form-login",
             response_model=TokenResponse,
             status_code=200)
async def form_login(data: Annotated[OAuth2PasswordRequestForm, Depends()],
                     session: AsyncSession = Depends(get_async_db_session)):
    """ """
    user = LoginRequest(email=data.username,
                        password=data.password)
    return await authenticate_user(user, session)



@router.post("/refresh",
             response_model=TokenResponse,
             status_code=200)
def refresh_token(
    request: RefreshRequest
):
    """
    Refresh token endpoint. Validates refresh token
    
    """
    token = request.refresh_token
    return get_refresh_token(token)


@router.post("/forgot-password",
            response_model=ResetTokenResponse,
            status_code=200)
async def forgot_password(
                    request: ForgotPasswordRequest,
                    db_session: AsyncSession = Depends(get_async_db_session)):
                    """Generates password reset mail and token"""
                    return await reset_password(request.email, db_session)


@router.post("/password-reset",
            response_model=PasswordResetResponse,
            status_code=200)
async def new_password(request: PasswordResetRequest,
                db_session: AsyncSession = Depends(get_async_db_session)):
                """Verifies password reset token and creates new password"""
                msg = await create_new_password(request.new_password, request.reset_token, db_session)
                if msg: 
                    return PasswordResetResponse(
                        msg=str(msg)
                    )
                else:
                       return PasswordResetResponse(
                              msg = "failed to reset password"
                       )


@router.post("/test-email",
            status_code=200)
async def test_email(email: str):
    """Test email functionality"""
    success = await send_test_email(email)
    if success:
        return {"message": f"Test email sent successfully to {email}"}
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to send test email to {email}"
        )

