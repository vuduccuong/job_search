#  __author__ = "Vũ Đức Cường"
#  ___date__ = 9/28/22, 10:38 AM
from typing import Optional

from pydantic import BaseModel, Field


class CompanyBase(BaseModel):
    name: str
    address: str
    employee_total: int = Field(gt=0)
    website: Optional[str]


class CreateCompanyVM(CompanyBase):
    pass
