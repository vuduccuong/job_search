#  __author__ = "Vũ Đức Cường"
#  ___date__ = 11/6/22, 2:28 PM
from fastapi import HTTPException
from starlette import status


class YoutubeException(Exception):
    @classmethod
    def search_exception(
        cls, status_code: int = status.HTTP_400_BAD_REQUEST, message: str = ""
    ):
        return HTTPException(
            status_code=status_code,
            detail=message,
            headers={"WWW-RegexMatch": "Error"},
        )
