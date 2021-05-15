"""This file contains handlers for api."""
import io

from flask import jsonify, request, send_file

from booking_api.app import app, cache, local_storage_manager
from booking_api.constants import CACHE_DEFAULT_TIMEOUT as timeout
from booking_api.database.database_structure import (Apartament, Booking,
                                                     ExtendedRating, Hotel,
                                                     User)


@app.route('/')
@cache.cached(timeout=timeout)
def index():
    """Return index page."""
    # Checks that redis cache works.
    from datetime import datetime
    return f"Already cached in {datetime.now().time().replace(microsecond=0)} for {timeout} sec."


@app.route('/api/hotels', methods=['GET'])
@cache.cached(timeout=timeout)
def get_hotels():
    """Return all hotels with several parameters."""
    hotels = Hotel.get_all(request)

    return jsonify(hotels)


@app.route('/api/apartaments', methods=['GET'])
@cache.cached(timeout=timeout)
def get_apartaments():
    """Return all apartaments with several parameters."""
    apartaments = Apartament.get_all(request)

    return jsonify(apartaments)


@app.route('/api/extended_rating', methods=['GET'])
@cache.cached(timeout=timeout)
def get_extended_rating():
    """Return extended rating by hotel_id."""
    ext_rating = ExtendedRating.get_all(request)

    return jsonify(ext_rating)


@app.route('/api/booking', methods=['GET'])
@cache.cached(timeout=timeout)
def get_booking():
    """Return all bookings by user_id."""
    booking = Booking.get_all(request)

    return jsonify(booking)


@app.route('/api/users', methods=['GET'])
@cache.cached(timeout=timeout)
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


@app.route('/api/hotels_post', methods=['POST'])
def post_hotel():
    """Book hotel rooms."""
    return 'Hotels received with args'


@app.route('/api/hotels_put', methods=['PUT'])
def put_hotel():
    """Сhange room and booking dates."""
    return 'Booking for user id'


@app.route('/api/hotels_delete', methods=['DELETE'])
def delete_booking():
    """Delete booking."""
    return 'Booking deleted with args'
