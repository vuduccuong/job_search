#  __author__ = "Vũ Đức Cường"
#  ___date__ = 10/1/22, 1:55 PM
from typing import Mapping

from fastapi import APIRouter, Depends
from fastapi_pagination import Params
from sqlalchemy.orm import Session
from starlette import status

from core.dependency.get_current_user import get_current_user
from core.dependency.jwt_beare import JwtBearer
from jobsearch_auth.models import AppUser
from jobsearch_company.dependencies import valid_company_id
from jobsearch_company.schemas import CreateCompanyVM
from src.core.crud.company import CompanyRepository
from src.core.dependency.get_db import get_db

router = APIRouter(
    prefix="/companies",
    tags=["Company"],
    responses={status.HTTP_404_NOT_FOUND: {"details": "Company not found"}},
)


@router.get("/")
async def get_company(
    db: Session = Depends(get_db),
    params: Params = Depends(),
):
    return await CompanyRepository.get_all(db=db, params=params)


@router.post("/")
async def create_company(
    company: CreateCompanyVM,
    db: Session = Depends(get_db),
    user: AppUser = Depends(get_current_user),
):
    await CompanyRepository.create_company(company_vm=company, user_id=user.id, db=db)

    return {"status": status.HTTP_201_CREATED}


@router.get("/{company_id}/reviews")
async def get_company_reviews(company: Mapping = Depends(valid_company_id)):
    return company
