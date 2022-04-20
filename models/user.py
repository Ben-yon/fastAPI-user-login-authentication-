from config import SQLALCHEMY_DATABASE_URI
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy import Boolean, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel


engine = create_engine(SQLALCHEMY_DATABASE_URI)
metadata = sqlalchemy.MetaData(engine)
print(metadata)
metadata.reflect()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class User(BaseModel):
    __table__ = Table("res_users", metadata)
    