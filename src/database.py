#  __author__ = "Vũ Đức Cường"
#  ___date__ = 10/1/22, 1:52 PM

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://root:G7e3KSMED@localhost:3306/jobcare_dev"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, bind=engine)

Base = declarative_base()
