from fastapi import APIRouter, Depends, status, Request

from zeno.api.user.schemas import (
    UserCreate,
    UserResponse,
    LoginRequest,
    RegisterResponse,
    RefreshRequest,
    TokenResponse
)
from zeno.api.models.users import User
from zeno.api.core.db import get_db_session, Session
from zeno.api.user.service import (
    get_current_user,
    add_new_user,
    authenticate_user,
    get_refresh_token
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
    """
    return await authenticate_user(login_data, session)


@router.post("/refresh",
             response_model=TokenResponse,
             status_code=200)
def refresh_token(
    request: RefreshRequest
):
    token = request.refresh_token
    return get_refresh_token(token)
