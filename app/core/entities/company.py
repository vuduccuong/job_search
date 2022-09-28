#  __author__ = "Vũ Đức Cường"
#  ___date__ = 9/28/22, 9:36 AM
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from app.core.database import Base


class Company(Base):
    __tablename__ = "jobcare_companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True)
    address = Column(String(255))
    employee_total = Column(Integer)
    website = Column(String(255))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    created_by = Column(Integer)
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
    updated_by = Column(Integer)
