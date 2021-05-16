"""This module works with database."""
from typing import Any, Dict, List

from sqlalchemy import (Column, DateTime, Float, ForeignKey, Integer, String,
                        create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from werkzeug.local import LocalProxy

from booking_api.app import cache
from booking_api.constants import CACHE_DEFAULT_TIMOUT_DB as timeout_db
from booking_api.constants import SQL_STRING
from booking_api.validate_args import prepare_args, validate_args

Base: Any = declarative_base()

engine = create_engine(SQL_STRING)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


class Mixin():
    """Mixin class for database."""

    def to_dict(self):
        """Return class object as dict."""
        return self.__dict__

    @classmethod
    def to_json(cls, objects_list: List[Any]) -> List[Dict]:
        """Make from List[cls object] jsonify structure List[Dict]."""
        json_list = []
        for cls_object in objects_list:
            temp_dict = cls_object.to_dict()
            temp_dict.pop('_sa_instance_state', None)
            json_list.append(temp_dict)

        return json_list

    @classmethod
    @cache.memoize(timeout=timeout_db)
    def get_all(cls, request: LocalProxy) -> List[Dict]:
        """Get all rows from several database table."""
        args = prepare_args(cls, request)
        rows = session.query(cls).filter(*args).all()

        return cls.to_json(rows)


class User(Base, Mixin):  # noqa: D101
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    email = Column(String, nullable=True, unique=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    role = Column(String, nullable=False)

    booking = relationship('Booking')


class Booking(Base, Mixin):  # noqa: D101
    __tablename__ = 'booking'

    booking_id = Column(Integer, primary_key=True)
    hotel_id = Column(Integer, ForeignKey('hotel.hotel_id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    apartament_id = Column(Integer, ForeignKey('apartament.apartament_id'), nullable=False)
    date_in = Column(DateTime, nullable=False)
    date_out = Column(DateTime, nullable=False)

    @classmethod
    def create(cls, request: LocalProxy) -> str:
        args = validate_args(request)
        try:
            session.add(cls(**args))
            session.commit()
            return f"Added booking with {args}"
        except Exception as ex:
            session.rollback()
            return f"Cant create booking. Maybe there is no user, hotel or apartaments id. Exception: {ex}"

    @classmethod
    def delete(cls, request: LocalProxy) -> str:
        args = validate_args(request)
        booking = session.query(cls).filter_by(**args).first()
        try:
            session.delete(booking)
            session.commit()
            return f"Deleted with id {args}"
        except Exception as ex:
            session.rollback()
            return "Error while deleting, maybe booking with several id already does not exist." \
                   f"Exception: {ex}"

    @classmethod
    def update(cls, request: LocalProxy) -> None:
        args = validate_args(request)
        session.query(cls).update(args)


class Hotel(Base, Mixin):  # noqa: D101
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
    important_facilities = relationship('ImportantFacilities')
    neighborhood_structures = relationship('NeighborhoodStructures')
    services_offered = relationship('ServicesOffered')
    extended_rating = relationship('ExtendedRating')
    review_rating = relationship('ReviewRating')


class Apartament(Base, Mixin):  # noqa: D101
    __tablename__ = 'apartament'

    apartament_id = Column(Integer, primary_key=True)
    hotel_id = Column(Integer, ForeignKey('hotel.hotel_id'), nullable=False)
    name = Column(String)
    price = Column(Float, nullable=False)
    service_offered = Column(String)
    beds = Column(Integer)

    booking = relationship('Booking')


class Coordinates(Base, Mixin):  # noqa: D101
    __tablename__ = 'coordinates'

    hotel_id = Column(Integer, ForeignKey('hotel.hotel_id'), primary_key=True)
    latitude = Column(String, nullable=False)
    longitude = Column(String, nullable=False)


class ImportantFacilities(Base, Mixin):  # noqa: D101
    __tablename__ = 'important_facilities'

    hotel_id = Column(Integer, ForeignKey('hotel.hotel_id'), primary_key=True)
    important_facilities = Column(String, nullable=False)


class NeighborhoodStructures(Base, Mixin):  # noqa: D101
    __tablename__ = 'neighborhood_structures'

    neighborhood_structures_id = Column(Integer, primary_key=True)
    hotel_id = Column(Integer, ForeignKey('hotel.hotel_id'))
    neighborhood_structure = Column(String, nullable=True)
    structure_type = Column(String, nullable=False)
    distance = Column(String, nullable=False)


class ServicesOffered(Base, Mixin):  # noqa: D101
    __tablename__ = 'services_offered'

    services_offered_id = Column(Integer, primary_key=True)
    hotel_id = Column(Integer, ForeignKey('hotel.hotel_id'))
    services_offered = Column(String, nullable=False)
    service_value = Column(String, nullable=False)


class ExtendedRating(Base, Mixin):  # noqa: D101
    __tablename__ = 'extended_rating'

    extended_rating_id = Column(Integer, primary_key=True)
    hotel_id = Column(Integer, ForeignKey('hotel.hotel_id'))
    rating_name = Column(String, nullable=False)
    rating_value = Column(Float, nullable=False)


class ReviewRating(Base, Mixin):  # noqa: D101
    __tablename__ = 'review_rating'

    review_rating_id = Column(Integer, primary_key=True)
    hotel_id = Column(Integer, ForeignKey('hotel.hotel_id'))
    review_rating_name = Column(String, nullable=False)
    review_rating_count = Column(Integer, nullable=False)


Base.metadata.create_all(engine)
