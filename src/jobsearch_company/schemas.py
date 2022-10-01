#  __author__ = "Vũ Đức Cường"
#  ___date__ = 10/1/22, 1:55 PM
from typing import Optional

from pydantic import BaseModel, Field


class CompanyBase(BaseModel):
    name: str
    address: str
    employee_total: int = Field(gt=0)
    website: Optional[str]


class CreateCompanyVM(CompanyBase):
    pass
