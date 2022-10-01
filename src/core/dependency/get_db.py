#  __author__ = "Vũ Đức Cường"
#  ___date__ = 9/28/22, 10:24 AM
from typing import Generator

from database import SessionLocal


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
