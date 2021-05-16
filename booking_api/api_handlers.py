"""This file contains handlers for api."""
import io
from random import choice, randint, uniform

from flask import jsonify, redirect, request, send_file, url_for

from booking_api.app import app, cache, celery, local_storage_manager
from booking_api.constants import CACHE_DEFAULT_TIMEOUT as ctimeout
from booking_api.database.database_structure import (Apartament, Booking,
                                                     ExtendedRating, Hotel,
                                                     User, session)


@app.route('/')
@cache.cached(timeout=ctimeout)
def index():
    """Return index page."""
    # Checks that redis cache works.
    from datetime import datetime
    return f"Already cached in {datetime.now().time().replace(microsecond=0)} for {ctimeout} sec."


@app.route('/api/hotels', methods=['GET'])
@cache.cached(timeout=ctimeout)
def get_hotels():
    """Return all hotels with several parameters."""
    hotels = Hotel.get_all(request)

    return jsonify(hotels)


@app.route('/api/apartaments', methods=['GET'])
@cache.cached(timeout=ctimeout)
def get_apartaments():
    """Return all apartaments with several parameters."""
    apartaments = Apartament.get_all(request)

    return jsonify(apartaments)


@app.route('/api/extended_rating', methods=['GET'])
@cache.cached(timeout=ctimeout)
def get_extended_rating():
    """Return extended rating by hotel_id."""
    ext_rating = ExtendedRating.get_all(request)

    return jsonify(ext_rating)


@app.route('/api/booking', methods=['GET'])
@cache.cached(timeout=ctimeout)
def get_booking():
    """Return all bookings by user_id."""
    booking = Booking.get_all(request)

    return jsonify(booking)


@app.route('/api/users', methods=['GET'])
@cache.cached(timeout=ctimeout)
def get_users():
    """Return all users with several parameters."""
    users = User.get_all(request)

    return jsonify(users)


@app.route('/api/documentation', methods=['GET'])
def get_documentation():
    """Return documentation file."""
    return send_file(
        io.BytesIO(local_storage_manager.get_api_documentation()),
        mimetype='text/yaml',
        attachment_filename='api_documentation.yaml',
        as_attachment=True,
    )


@app.route('/api/booking/create', methods=['POST'])
def create_booking():
    """Book hotel rooms."""
    Booking.create(request)
    return redirect(url_for('get_booking'))


@app.route('/api/booking/update', methods=['PUT'])
def update_booking():
    """Book hotel rooms."""
    Booking.update(request)
    return redirect(url_for('get_booking'))


@app.route('/api/booking/delete', methods=['DELETE'])
def delete_booking():
    """Delete booking."""
    Booking.delete(request)
    return redirect(url_for('get_booking'))


@app.route('/api/insert_pseudo')
def insert_pseudo():
    """Insert pseudo hotels."""
    hotels_insert.delay()
    return redirect(url_for('api/hotels'))


@celery.task(name='celery.insert_pseudo')
def hotels_insert():
    """Insert pseudo hotels."""
    hotel_names = ['First World Hotel & Plaza', 'CityCenter', 'MGM Grand', 'Ambassador City Jomtien',
                   'Hotel Paris', 'Four Seasons Hotel Firenze', 'Laurus Al Duomo',
                   'NH Collection Firenze Porta Rossa', 'Grand Hotel Minerva']
    apartaments_names = ['Улучшенный номер с кроватью размера «king-size»',
                         'Номер Делюкс с кроватью размера «king-size»',
                         'Люкс "Салон"', 'Представительский люкс Four Seasons с кроватью размера "king-size"',
                         'Представительский люкс с кроватью размера «king-size» - Вид на собор',
                         'Люкс с кроватью размера «king-size» и видом на бассейн и сад',
                         'Королевский люкс с кроватью размера «king-size»',
                         'Номер "Четыре сезона" с кроватью размера "king-size"']

    cities = ['Jakarta', 'Manila', 'Istanbul', 'Lagos', 'Paris', 'London', 'Toronto']
    for _index in range(randint(1, 10)):
        hotel_obj = Hotel(
            name=choice(hotel_names),
            stars=randint(1, 5),
            rating=round(uniform(0, 10), 2),
            price=randint(1000, 15000),
            city=choice(cities),
        )

        for _index in range(randint(1, 10)):
            apartament_obj = Apartament(
                name=choice(apartaments_names),
                price=randint(1000, 15000),
                beds=randint(1, 4),
            )
            hotel_obj.apartament.append(apartament_obj)

        session.add(hotel_obj)
    session.commit()
