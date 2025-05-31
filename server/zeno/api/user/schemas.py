from pydantic import BaseModel


class user(BaseModel):
    username: str
    email: str
    is_verified: bool = False


class UserCreate(BaseModel):
    username: str
    email: str
    password: str

