from fastapi import Depends, HTTPException, status
from zeno.api.user.schemas import UserBase


def get_current_user(user: UserBase):
    pass
