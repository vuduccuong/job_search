#  __author__ = "Vũ Đức Cường"
#  ___date__ = 10/2/22, 8:12 PM
from sqlalchemy.orm import Session

from core.services.password import PasswordService
from jobsearch_auth.exceptions import AuthException
from jobsearch_auth.models import AppUser


class AuthService:
    @classmethod
    def authenticate_user(cls, username: str, password: str, db: Session):
        user = db.query(AppUser).filter(AppUser.username == username).first()
        if not user:
            raise AuthException.get_user_exception()
        if not PasswordService.verify_password(password, user.hash_password):
            raise AuthException.token_exception()

        return user
