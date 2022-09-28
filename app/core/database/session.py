#  __author__ = "Vũ Đức Cường"
#  ___date__ = 9/28/22, 9:53 AM
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = (
    "mysql+mysqldb://root:mysqlpw@host.docker.internal:49153/jobcare_dev"
)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, bind=engine)
