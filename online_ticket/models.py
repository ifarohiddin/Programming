from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:///ticket.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False},echo=True)
session = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()


class Ticket(Base):
    __tablename__ = "ticket"
    id = Column(Integer, primary_key=True, index=True)
    flight = relationship('Flight', back_populates='tickets')
    flight_id = Column(Integer, ForeignKey('flight.id'))
    price = Column(Integer)
    data_form = Column(DateTime, nullable=False)
    data_to = Column(DateTime, nullable=False)
    passengers = relationship('Passenger', back_populates='tickett')
    passenger_id = Column(Integer, ForeignKey('passenger.id'))


class Flight(Base):
    __tablename__ = "flight"
    id = Column(Integer, primary_key=True, index=True)
    space_count = Column(Integer)
    from_city = Column(String)
    to_city = Column(String)
    tickets = relationship('Ticket', back_populates='flight')


class Order(Base):
    __tablename__ = "order"
    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(Integer, ForeignKey('ticket.id'))
    amount = Column(Integer)

class Passenger(Base):
    __tablename__ = "passenger"
    id = Column(Integer, primary_key=True, index=True)
    tickett = relationship('Ticket', back_populates='passengers')
    passport = Column(Integer)
    first_name = Column(String)
    last_name = Column(String)

Base.metadata.create_all(bind=engine)