from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Response, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
import structlog

LOG = structlog.stdlib.get_logger()

router = APIRouter()
oauth2scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

@router.get("/heartbeat", tags = ['server'])
@router.get("/heartbeat/", tags= ["server"])
def get_heartbeat():
    pass 

@router.post("/auth/register")
def register():
    pass


@router.post("/auth/login")
def login():
    pass

async def get_current_user(token: str=Depends(oauth2scheme), db: Session=Depends(get_db))
@router.get("/users/me")
def get_user():
    pass
    