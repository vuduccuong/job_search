#  __author__ = "Vũ Đức Cường"
#  ___date__ = 10/1/22, 5:23 PM
from typing import Union, Dict

from fastapi import HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from starlette.requests import Request

from jobsearch_auth.utils import decode_jwt


class JwtBearer(HTTPBearer):
    def __init__(self):
        super(JwtBearer, self).__init__()

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(
            JwtBearer, self
        ).__call__(request)
        if credentials:
            if credentials.scheme != "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authentication scheme."
                )
            payload = self.verify_jwt(credentials.credentials)
            if not payload:
                raise HTTPException(
                    status_code=403, detail="Invalid token or expired token."
                )
            return payload
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    # noinspection PyMethodMayBeStatic
    def verify_jwt(self, jwtoken: str) -> Union[Dict, None]:
        try:
            return decode_jwt(jwtoken)
        except Exception as ex:
            print(ex)
        return None
