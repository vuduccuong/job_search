#  __author__ = "Vũ Đức Cường"
#  ___date__ = 9/28/22, 10:29 AM

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from jobsearch_company.router import router as company_router
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(company_router)

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", context={"request": request})
