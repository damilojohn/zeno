from typing import Annotated
from fastapi import APIRouter, Depends, status
from fastapi.background import P
from fastapi.security import OAuth2PasswordRequestForm

from zeno.api.user.schemas import (
    UserCreate,
    UserResponse,
    LoginRequest,
    RegisterResponse,
    RefreshRequest,
    TokenResponse,
    PasswordResetRequest,
    PasswordResetResponse,
    ResetTokenResponse
)

from zeno.api.models.users import User
from zeno.api.core.db import get_db_session, Session
from zeno.api.user.service import (
    get_current_user,
    add_new_user,
    authenticate_user,
    get_refresh_token,
    reset_password,
    create_new_password
)

router = APIRouter(prefix="/v2/auth", tags=["users"])



@router.get("/me", response_model=UserResponse)
async def get_user_profile(
    user: User = Depends(get_current_user)
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
    session: Session = Depends(get_db_session)
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
    session: Session = Depends(get_db_session)
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
                     session = Depends(get_db_session)):
    """ """
    user = LoginRequest(username=data.username,
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
def forgot_password(
                    user: User = Depends(get_current_user),
                    db_session: Session = Depends(get_db_session)):
                    """Generates password reset mail and token"""
                    return reset_password(user, db_session)


@router.post("/password-reset",
            response_model=PasswordResetResponse,
            status_code=200)
def new_password(request: PasswordResetRequest,
                user = Depends(get_current_user),
                db_session = Depends(get_db_session)):
                """Verifies password reset token and creates new password"""
                msg = create_new_password(request.new_password,user, request.reset_token, db_session)
                if msg:
                       
                    return PasswordResetResponse(
                        msg=str(msg)
                    )
                else:
                       return PasswordResetResponse(
                              msg = "failed to reset password"
                       )

