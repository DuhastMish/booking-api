"""This module works with database."""
from typing import Any

from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base: Any = declarative_base()
engine = None
session = None


class User(Base):  # noqa: D101
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    email = Column(String, nullable=True, unique=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    role = Column(String, nullable=False)


class Booking(Base):  # noqa: D101
    __tablename__ = 'booking'

    booking_id = Column(Integer, primary_key=True)
    hotel_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    apartament_id = Column(Integer, nullable=False)
    date_in = Column(DateTime, nullable=False)
    date_out = Column(DateTime, nullable=False)


class Hotel(Base):  # noqa: D101
    __tablename__ = 'hotel'

    hotel_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    stars = Column(Integer)
    rating = Column(Float)
    price = Column(Float, nullable=False)
    image = Column(String)
    city = Column(String, nullable=False)
    extended_rating = Column(String)


class Apartament(Base):  # noqa: D101
    __tablename__ = 'apartament'

    apartament_id = Column(Integer, primary_key=True)
    hotel_id = Column(Integer, nullable=False)
    name = Column(String)
    price = Column(Float, nullable=False)
    service_offered = Column(String)
    beds = Column(Integer)
