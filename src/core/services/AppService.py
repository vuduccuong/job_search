#  __author__ = "Vũ Đức Cường"
#  ___date__ = 11/6/22, 4:36 PM
from sqlalchemy.orm import Session


class DBSessionMixin:
    def __init__(self, db: Session):
        self.db = db


class AppService(DBSessionMixin):
    pass
