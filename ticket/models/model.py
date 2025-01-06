from sqlalchemy import create_engine, Column,Integer,String,DateTime,EmailStr
from sqlalchemy.orm import declarative_base,sessionmaker,relationship
from sqlalchemy_utils import EmailType
from dotenv import load_dotenv
load_dotenv()

import os
user_db = os.getenv("USER_DB")
pass_db = os.getenv("PASS_DB")
name_db = os.getenv("NAME_DB")

DATABASE_URL = 'postgresql://{settings.user_db}:{settings.pass_db}#1984@localhost/{settings.name_db}'
engine = create_engine(DATABASE_URL)
session = sessionmaker
Base = declarative_base()

class Flights(Base):
    __tablename__ = 'flights'
    id=Column(int,primary_key=True,index=True)
    flight_number = Column(str,index=True)
    to_city = Column(str)
    plane_id=relationship("Plane",back_populates="flight")
    date_time=Column(DateTime)

class Plane(Base):
    __tablename__ = 'plane'
    id = Column(int,primary_key=True,index=True)
    plane_model=Column(str)
    space_bus =Column(int)
    space_eco=Column(int)
    flight=relationship('Flights',back_populates='plane_id')

class Passenger(Base):
    __tablename__ = 'passenger'
    fullname:Column(str)
    passport_id:Column(str,index=True)
    phone_number:Column(int)
    birth_date:Column(DateTime)
    email:Column(EmailType)