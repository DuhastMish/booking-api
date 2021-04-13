"""This module works with database."""
from typing import Any

from sqlalchemy import (Column, DateTime, Float, ForeignKey, Integer, String,
                        create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base: Any = declarative_base()
SQL_STRING = 'postgresql://username:password@localhost:5432/dbname'
engine = create_engine(SQL_STRING)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


class User(Base):  # noqa: D101
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    email = Column(String, nullable=True, unique=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    role = Column(String, nullable=False)

    booking = relationship('Booking')


class Booking(Base):  # noqa: D101
    __tablename__ = 'booking'

    booking_id = Column(Integer, primary_key=True)
    hotel_id = Column(Integer, ForeignKey('hotel.hotel_id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    apartament_id = Column(Integer, ForeignKey('apartament.apartament_id'), nullable=False)
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

    booking = relationship('Booking')
    apartament = relationship('Apartament')
    coordinates = relationship('Coordinates')
    importantFacilities = relationship('ImportantFacilities')
    neighborhoodStructures = relationship('NeighborhoodStructures')
    servicesOffered = relationship('ServicesOffered')
    extendedRating = relationship('ExtendedRating')
    reviewRating = relationship('ReviewRating')
    
    
class Apartament(Base):  # noqa: D101
    __tablename__ = 'apartament'

    apartament_id = Column(Integer, primary_key=True)
    hotel_id = Column(Integer, ForeignKey('hotel.hotel_id'), nullable=False)
    name = Column(String)
    price = Column(Float, nullable=False)
    service_offered = Column(String)
    beds = Column(Integer)

    booking = relationship('Booking')


class Coordinates(Base):  # noqa: D101
    __tablename__ = 'coordinates'

    hotel_id = Column(Integer, ForeignKey('hotel.hotel_id'), primary_key=True)
    latitude = Column(String, nullable=False)
    longitude = Column(String, nullable=False)

    

class ImportantFacilities(Base):  # noqa: D101
    __tablename__ = 'important_facilities'

    hotel_id = Column(Integer, ForeignKey('hotel.hotel_id'), primary_key=True)
    important_facilities = Column(String, nullable=False)


class NeighborhoodStructures(Base):  # noqa: D101
    __tablename__ = 'neighborhood_structures'

    neighborhood_structures_id = Column(Integer, primary_key=True)
    hotel_id = Column(Integer, ForeignKey('hotel.hotel_id'))
    neighborhood_structure = Column(String, nullable=True)
    structure_type = Column(String, nullable=False)
    distance = Column(String, nullable=False)


class ServicesOffered(Base):  # noqa: D101
    __tablename__ = 'services_offered'

    services_offered_id = Column(Integer, primary_key=True)
    hotel_id = Column(Integer, ForeignKey('hotel.hotel_id'))
    services_offered = Column(String, nullable=False)
    service_value = Column(String, nullable=False)


class ExtendedRating(Base):  # noqa: D101
    __tablename__ = 'extended_rating'

    extended_rating_id = Column(Integer, primary_key=True)
    hotel_id = Column(Integer, ForeignKey('hotel.hotel_id'))
    rating_name = Column(String, nullable=False)
    rating_value = Column(Float, nullable=False)


class ReviewRating(Base):  # noqa: D101
    __tablename__ = 'review_rating'

    review_rating_id = Column(Integer, primary_key=True)
    hotel_id = Column(Integer, ForeignKey('hotel.hotel_id'))
    review_rating_name = Column(String, nullable=False)
    review_rating_count = Column(Integer, nullable=False)
