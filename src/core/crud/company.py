#  __author__ = "Vũ Đức Cường"
#  ___date__ = 9/28/22, 10:14 AM
from typing import Optional, Dict

from sqlalchemy.orm import Session

from jobsearch_company.models import Company
from jobsearch_company.schemas import CreateCompanyVM
from fastapi_pagination import Params, paginate


class CompanyRepository:
    @classmethod
    async def get_all(cls, db: Session, params: Params):
        query_set = db.query(Company).all()
        return paginate(query_set, params)

    @classmethod
    async def create_company(
        cls, company_vm: CreateCompanyVM, user_id: int, db: Session
    ):
        company_entity = Company()
        company_entity.name = company_vm.name
        company_entity.address = company_vm.address
        company_entity.employee_total = company_vm.employee_total
        company_entity.website = company_vm.website
        company_entity.created_by = user_id
        company_entity.updated_by = user_id

        db.add(company_entity)
        db.commit()
