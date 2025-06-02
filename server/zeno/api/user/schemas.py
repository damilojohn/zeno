from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    is_verified: bool = False


class UserCreate(UserBase):
    password: str
