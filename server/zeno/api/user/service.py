from typing import Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from datetime import datetime, timedelta

from zeno.api.user.models import User, SearchHistory
from zeno.api.user.schemas import UserCreate, UserOAuthCreate
from zeno.api.core.security import (
    get_password_hash,
    verify_password,
    create_access_token,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)


class UserService:
    def __init__(self, db: Session):
        self.db = db

    async def get_user_by_email(self, email: str) -> Optional[User]:
        return self.db.query(User).filter(User.email == email).first()

    async def create_user(self, user_data: UserCreate) -> User:
        # Check if user exists
        db_user = await self.get_user_by_email(email=user_data.email)
        if db_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        
        # Create new user
        hashed_password = get_password_hash(user_data.password)
        db_user = User(
            email=user_data.email,
            hashed_password=hashed_password,
            is_oauth_user=False
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    async def create_oauth_user(self, user_data: UserOAuthCreate) -> User:
        # Check if user exists
        db_user = await self.get_user_by_email(email=user_data.email)
        if db_user:
            if not db_user.is_oauth_user:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Email already registered with password"
                )
            return db_user
        
        # Create new OAuth user
        db_user = User(
            email=user_data.email,
            is_oauth_user=True,
            oauth_provider=user_data.oauth_provider
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    async def authenticate_user(self, email: str, password: str) -> Optional[User]:
        user = await self.get_user_by_email(email)
        if not user or user.is_oauth_user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    async def create_user_token(self, user: User) -> dict:
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.email},
            expires_delta=access_token_expires
        )
        return {
            "access_token": access_token,
            "token_type": "bearer"
        }

    async def add_search_history(self, user_id: int, query: str, results: dict):
        search_history = SearchHistory(
            user_id=user_id,
            query=query,
            results=results
        )
        self.db.add(search_history)
        self.db.commit()
        self.db.refresh(search_history)
        return search_history

    async def get_user_search_history(self, user_id: int):
        return (
            self.db.query(SearchHistory)
            .filter(SearchHistory.user_id == user_id)
            .order_by(SearchHistory.created_at.desc())
            .all()
        ) 