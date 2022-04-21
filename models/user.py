from config import SQLALCHEMY_DATABASE_URI
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


engine = create_engine(SQLALCHEMY_DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
# Base.query = SessionLocal.query_property()


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    username = Column(String, index=True)
    password = Column(String, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)


    