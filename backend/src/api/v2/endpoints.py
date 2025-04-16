from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Response
from fastapi
import structlog

LOG = structlog.stdlib.get_logger()

router = APIRouter()

@router.get("/heartbeat", tags = ['server'])
@router.get("/heartbeat/", tags= ["server"])

def get_heartbeat():
    pass 

@router.get("/users")
async def get_user(user_name):
    