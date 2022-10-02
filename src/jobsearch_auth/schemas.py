#  __author__ = "Vũ Đức Cường"
#  ___date__ = 10/1/22, 5:29 PM
from typing import Optional

from pydantic import BaseModel


class CreateUserSchema(BaseModel):
    username: str
    email: Optional[str]
    first_name: str
    last_name: str
    password: str


class LoginUserSchema(BaseModel):
    username: str
    password: str
