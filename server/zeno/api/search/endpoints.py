from fastapi import APIRouter, Depends, status

from zeno.api.search.schemas import SearchRequest
# from zeno.api.search.service import



router = APIRouter(prefix="/api/v2/search", tags=['search'])


# @router.post("/",
#              response_model=,
#              status_code=200)

# async def search
