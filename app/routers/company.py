#  __author__ = "Vũ Đức Cường"
#  ___date__ = 9/28/22, 9:33 AM
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from app.core.crud.company import CompanyRepository
from app.core.dependency.get_db import get_db
from app.schemas.company import CreateCompanyVM

router = APIRouter(
    prefix="/companies",
    tags=["Company"],
    dependencies=[],
    responses={status.HTTP_404_NOT_FOUND: {"details": "Company not found"}},
)


@router.get("/")
async def get_company(db: Session = Depends(get_db)):
    return await CompanyRepository.get_all(db=db)


@router.post("/")
async def create_company(company: CreateCompanyVM, db: Session = Depends(get_db)):
    await CompanyRepository.create_company(company_vm=company, db=db)

    return {"status": status.HTTP_201_CREATED}
