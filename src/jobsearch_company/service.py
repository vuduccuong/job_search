#  __author__ = "Vũ Đức Cường"
#  ___date__ = 10/1/22, 1:56 PM
from core.services.AppService import AppService
from jobsearch_company.exceptions import CompanyException
from jobsearch_company.models import Company


class CompanyService(AppService):
    async def get_by_id(self, company_id: int):
        company = self.db.query(Company).get(company_id)
        if not company:
            raise CompanyException.not_found_company()
        return company
