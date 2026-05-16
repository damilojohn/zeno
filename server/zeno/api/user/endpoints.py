from typing import Annotated
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from zeno.api.user.schemas import (
    UserCreate,
    UserResponse,
    LoginRequest,
    RegisterResponse,
    RefreshRequest,
    TokenResponse,
    GoogleAuthRequest,
    GoogleAuthResponse,
    ForgotPasswordRequest,
    PasswordResetRequest,
)
from zeno.api.core.db import get_async_db_session
from zeno.api.core.responses import ApiResponse
from zeno.api.core.exceptions import InternalServerError
from zeno.api.user.service import (
    get_current_user,
    add_new_user,
    authenticate_user,
    handle_google_oauth,
    get_refresh_token,
    reset_password,
    create_new_password,
)
from zeno.api.core.email import send_test_email

router = APIRouter(prefix="/v2/auth", tags=["users"])


@router.get("/heartbeat", response_model=ApiResponse[None])
def heartbeat():
    return ApiResponse(msg="ok")


@router.get("/me", response_model=ApiResponse[UserResponse])
async def get_user_profile(user: UserResponse = Depends(get_current_user)):
    return ApiResponse(data=user)


@router.post(
    "/sign-up",
    response_model=ApiResponse[RegisterResponse],
    status_code=status.HTTP_201_CREATED,
)
async def register_user(
    user: UserCreate, session: AsyncSession = Depends(get_async_db_session)
):
    result = await add_new_user(user, session)
    return ApiResponse(msg="User created successfully", data=result)


@router.post("/login", response_model=ApiResponse[TokenResponse])
async def login(
    login_data: LoginRequest, session: AsyncSession = Depends(get_async_db_session)
):
    result = await authenticate_user(login_data, session)
    return ApiResponse(msg="Login successful", data=result)


@router.post("/google", response_model=ApiResponse[GoogleAuthResponse])
async def google_auth(
    auth_request: GoogleAuthRequest,
    session: AsyncSession = Depends(get_async_db_session),
):
    result = await handle_google_oauth(
        auth_request.id_token, auth_request.redirect_uri, session
    )
    return ApiResponse(msg="Authenticated successfully", data=result)


@router.post("/form-login", response_model=ApiResponse[TokenResponse])
async def form_login(
    data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: AsyncSession = Depends(get_async_db_session),
):
    user = LoginRequest(email=data.username, password=data.password)
    result = await authenticate_user(user, session)
    return JSONResponse(
        status_code=200,
        content=result.model_dump()
    )


@router.post("/refresh", response_model=ApiResponse[TokenResponse])
def refresh_token(request: RefreshRequest):
    result = get_refresh_token(request.refresh_token)
    return ApiResponse(msg="Token refreshed", data=result)


@router.post("/forgot-password", response_model=ApiResponse[None])
async def forgot_password(
    request: ForgotPasswordRequest,
    db_session: AsyncSession = Depends(get_async_db_session),
):
    result = await reset_password(request.email, db_session)
    return ApiResponse(msg=result.msg)


@router.post("/password-reset", response_model=ApiResponse[None])
async def new_password(
    request: PasswordResetRequest,
    db_session: AsyncSession = Depends(get_async_db_session),
):
    msg = await create_new_password(request.new_password, request.reset_token, db_session)
    return ApiResponse(msg=str(msg) if msg else "Password reset failed")


@router.post("/test-email", response_model=ApiResponse[None])
async def test_email(email: str):
    success = await send_test_email(email)
    if not success:
        raise InternalServerError(f"Failed to send test email to {email}")
    return ApiResponse(msg=f"Test email sent to {email}")
