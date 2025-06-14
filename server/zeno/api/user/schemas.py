from pydantic import BaseModel, EmailStr, StringConstraints
from typing import Annotated


class UserBase(BaseModel):
    username: str
    email: str = ""
    is_verified: bool = False


class UserCreate(UserBase):
    password: Annotated[str, StringConstraints(
        strip_whitespace=True, max_length=64)]
    username: Annotated[str, StringConstraints(
        strip_whitespace=True, max_length=64)]


class UserResponse(UserBase):
    username: str
    is_verified: bool = False
    auth_provider: str = "local"  # local, google, apple


class RegisterResponse(BaseModel):
    username: str
    is_verified: bool = False
    access_token: str
    refresh_token: str
    message: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class LoginRequest(BaseModel):
    username: str
    email: str = ''
    password: str


class OAuthRequest(BaseModel):
    id_token: str
    redirect_uri: str


class OAuthResponse(BaseModel):
    user: UserResponse
    access_token: str
    refresh_token: str
    is_new_user: bool
