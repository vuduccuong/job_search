#  __author__ = "Vũ Đức Cường"
#  ___date__ = 10/1/22, 1:56 PM
from fastapi import HTTPException
from starlette import status


class CompanyException:
    @classmethod
    async def not_found_company(cls):
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Company Not Found",
        )
