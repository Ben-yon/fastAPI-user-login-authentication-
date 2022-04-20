from config import SQLALCHEMY_DATABASE_URI
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel


engine = create_engine(SQLALCHEMY_DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    username = Column(String, index=True)
    password = Column(String, index=True)
    is_active = Column(Boolean, default=True)

    