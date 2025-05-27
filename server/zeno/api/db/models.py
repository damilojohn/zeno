from backend.src.api.v2.db.session import Base

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import mapped_column
from pgvector.sqlalchemy import Vector


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    last_login = Column(DateTime, nullable=True)


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    _embeddings = mapped_column(Vector(728))
    title = Column(String, nullable=False)
    description = Column(String,)
    isbn = Column(Integer)
    categories = Column(Integer)
    authors = Column(String)
    thumbnail = Column(String)
    published_year = Column(String)
