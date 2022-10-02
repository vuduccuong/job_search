#  __author__ = "Vũ Đức Cường"
#  ___date__ = 10/2/22, 8:14 PM
from fastapi import HTTPException
from starlette import status


class AuthException:
    @classmethod
    def get_user_exception(cls):
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    @classmethod
    def token_exception(cls):
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrent username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
