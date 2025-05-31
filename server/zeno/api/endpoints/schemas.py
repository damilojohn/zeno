from pydantic import BaseModel


class User(BaseModel):
    username: str
    


class Book(BaseModel):
    title: str
    description: str
    thumbnail: str
    published_year: str


class UserCreate(BaseModel):
    username: str
