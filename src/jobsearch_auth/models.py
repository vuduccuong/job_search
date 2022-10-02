#  __author__ = "Vũ Đức Cường"
#  ___date__ = 10/1/22, 5:11 PM
from sqlalchemy import Column, Integer, String, Boolean

from database import Base


class AppUser(Base):
    __tablename__ = "jobsearch_users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255))
    username = Column(String(50))
    first_name = Column(String(100))
    last_name = Column(String(100))
    hash_password = Column(String(255))
    is_active = Column(Boolean, default=True)
