#  __author__ = "Vũ Đức Cường"
#  ___date__ = 10/1/22, 5:03 PM
from datetime import datetime, timedelta
from typing import Dict, Optional

import jwt
from decouple import config

from jobsearch_auth.models import AppUser

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")


def token_response(token: str):
    return {
        "access_token": token,
        "token_type": "bearer",
    }


def sign_jwt(user: AppUser) -> Dict[str, str]:
    expire = datetime.utcnow() + timedelta(minutes=15)
    payload = {"user_id": user.id, "exp": expire}
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    res = token_response(token)
    return res


def decode_jwt(token: str) -> Optional[dict]:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token
    except Exception as ex:
        print(ex)
        return {}
