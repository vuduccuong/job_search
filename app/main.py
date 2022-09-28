#  __author__ = "Vũ Đức Cường"
#  ___date__ = 9/28/22, 10:29 AM

from fastapi import FastAPI

from app.core.database import Base, engine
from app.routers import company


Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(company.router)
