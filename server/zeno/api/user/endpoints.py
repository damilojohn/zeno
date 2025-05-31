from fastapi import APIRouter, Depends

from zeno.api.models.users import



router = APIRouter(prefix="/users",)


@router.get("/me")
def get_user_profile(session:Depends(get_sync_session)):
