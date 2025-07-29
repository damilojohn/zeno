from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Response, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from zeno.api.core.db import get_db_session
from backend.src.api.v2.endpoints.schemas import UserCreate
import structlog

LOG = structlog.stdlib.get_logger()

router = APIRouter()
oauth2scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

@router.get("/heartbeat", tags = ['server'])
@router.get("/heartbeat/", tags= ["server"])
async def get_heartbeat(db: Session=Depends(get_db_session)):
    try:
        await db.execute("SELECT 1")
    except SQLAlchemyError as e:
        LOG.error(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Database connection failed") from e
    # TODO: Check other services
    return {"status": "ok"}


@router.post("/auth/register")
def register(user: UserCreate, db: Session=Depends(get_db_session)):
    


@router.post("/auth/login")
def login():
    pass

async def get_current_user(token: str=Depends(oauth2scheme), db: Session=Depends(get_db_session)):

@router.get("/users/me")
def get_user():
    
    