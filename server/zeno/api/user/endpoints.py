from fastapi import APIRouter, Depends


from zeno.api.user.schemas import UserCreate, UserBase
from zeno.api.core.db import get_db_session, Session
from zeno.api.user.service import get_current_user


router = APIRouter(prefix="/v2/users",
                   tags=["users"])


@router.get("/me")
def get_user_profile(session: Session = Depends(get_db_session),
                     user: UserBase = Depends(get_current_user)):
    pass
