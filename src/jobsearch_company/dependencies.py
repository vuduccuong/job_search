#  __author__ = "Vũ Đức Cường"
#  ___date__ = 10/1/22, 1:56 PM
from typing import Mapping

from fastapi import Depends
from sqlalchemy.orm import Session

from core.dependency.get_db import get_db
from jobsearch_company.service import CompanyService


async def valid_company_id(company_id: int, db: Session = Depends(get_db)) -> Mapping:
    return await CompanyService(db).get_by_id(company_id)
