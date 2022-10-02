#  __author__ = "Vũ Đức Cường"
#  ___date__ = 10/1/22, 5:14 PM
from typing import Optional

from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from starlette.requests import Request

from core.dependency.get_db import get_db
from core.services.password import PasswordService
from jobsearch_auth.exceptions import AuthException
from jobsearch_auth.models import AppUser
from jobsearch_auth.schemas import CreateUserSchema, LoginUserSchema
from jobsearch_auth.service import AuthService
from jobsearch_auth.utils import sign_jwt

# oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/login")
router = APIRouter(prefix="/auth", tags=["Auth"])


@router.get("/")
async def get_users(q: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(AppUser)
    if q:
        query = query.filter(AppUser.email == q)

    return query.all()


@router.post("/")
async def create_user(
    user: CreateUserSchema = Body(...), db: Session = Depends(get_db)
):
    user_entity = AppUser()
    user_entity.username = user.username
    user_entity.email = user.email
    user_entity.first_name = user.first_name
    user_entity.last_name = user.last_name
    user_entity.hash_password = PasswordService().get_password_hash(user.password)

    db.add(user_entity)
    db.commit()

    return user_entity


@router.post("/login")
async def login(user: LoginUserSchema, db: Session = Depends(get_db)):
    user = AuthService.authenticate_user(
        username=user.username, password=user.password, db=db
    )

    if not user:
        raise AuthException.get_user_exception()

    return sign_jwt(user)
