from typing import Annotated
from pydantic import UUID4, BaseModel, EmailStr, StringConstraints


class UserBase(BaseModel):
    email: EmailStr | None
    is_verified: bool = False


class UserCreate(UserBase):
    password: Annotated[str, StringConstraints(
        strip_whitespace=True, max_length=64)]
    # username: Annotated[str, StringConstraints(
    #     strip_whitespace=True, max_length=64)]


class UserResponse(UserBase):
    id: UUID4
    is_verified: bool = False
    auth_provider: str = "local"  # local, google, apple


class RegisterResponse(BaseModel):
    email: EmailStr
    is_verified: bool = False
    access_token: str
    refresh_token: str
    message: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class RefreshRequest(BaseModel):
    refresh_token: str
    token_type: str = "bearer"


class LoginRequest(BaseModel):
    email: EmailStr | None = None
    password: str


class GoogleAuthRequest(BaseModel):
    id_token: str
    redirect_uri: str


class GoogleAuthResponse(BaseModel):
    user: UserResponse
    access_token: str
    refresh_token: str
    message: str


class ForgotPasswordRequest(BaseModel):
    email: str


class PasswordResetRequest(BaseModel):
    reset_token:str
    new_password: str


class PasswordResetResponse(BaseModel):
    msg: str


class ResetTokenResponse(BaseModel):
    msg:str