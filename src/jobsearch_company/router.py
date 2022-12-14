#  __author__ = "Vũ Đức Cường"
#  ___date__ = 10/1/22, 1:55 PM
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from core.dependency.get_current_user import get_current_user
from jobsearch_auth.models import AppUser
from jobsearch_company.schemas import CreateCompanyVM
from src.core.crud.company import CompanyRepository
from src.core.dependency.get_db import get_db

router = APIRouter(
    prefix="/companies",
    tags=["Company"],
    # dependencies=[Depends(JwtBearer())],
    responses={status.HTTP_404_NOT_FOUND: {"details": "Company not found"}},
)


@router.get("/")
async def get_company(db: Session = Depends(get_db)):
    return await CompanyRepository.get_all(db=db)


@router.post("/")
async def create_company(
    company: CreateCompanyVM,
    db: Session = Depends(get_db),
    user: AppUser = Depends(get_current_user),
):
    await CompanyRepository.create_company(company_vm=company, user_id=user.id, db=db)

    return {"status": status.HTTP_201_CREATED}
