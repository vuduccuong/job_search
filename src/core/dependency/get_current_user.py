#  __author__ = "Vũ Đức Cường"
#  ___date__ = 10/2/22, 8:41 PM
from typing import Dict

from fastapi import Depends
from jwt import PyJWTError
from sqlalchemy.orm import Session

from core.dependency.get_db import get_db
from core.dependency.jwt_beare import JwtBearer
from jobsearch_auth.exceptions import AuthException
from jobsearch_auth.models import AppUser


async def get_current_user(
    user: Dict = Depends(JwtBearer()), db: Session = Depends(get_db)
):
    try:
        user_id: int = user.get("user_id")
        if not user_id:
            raise AuthException.get_user_exception()
        user = db.query(AppUser).filter(AppUser.id == user_id).first()
        if not user:
            raise AuthException.get_user_exception()

        return user
    except PyJWTError:
        raise AuthException.token_exception()
