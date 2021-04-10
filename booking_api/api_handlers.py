"""This file contains handlers for api."""
import io

from flask import request, send_file

from booking_api.app import app, local_storage_manager
from booking_api.validate_args import validate_args


@app.route('/')
def index():
    """Return index page."""
    return 'Hello, World!'


@app.route('/api/hotels', methods=['GET'])
def get_hotels():
    """Return all hotels with several parameters."""
    args = validate_args(request)
    return f'Hotels received with args: {args}'


@app.route('/api/apartaments', methods=['GET'])
def get_apartaments():
    """Return all apartaments with several parameters."""
    args = validate_args(request)
    return f'Apartaments received with args: {args}'


@app.route('/api/extended_rating', methods=['GET'])
def get_extended_rating():
    """Return extended rating by hotel_id."""
    args = validate_args(request)
    return f'Extended rating for hotel id: {args}'


@app.route('/api/booking', methods=['GET'])
def get_booking():
    """Return all bookings by user_id."""
    args = validate_args(request)
    return f'Booking for user id: {args}'


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
    args = validate_args(request)
    return f'Hotels received with args: {args}'


@app.route('/api/hotels_put', methods=['PUT'])
def put_hotel():
    """Сhange room and booking dates."""
    args = validate_args(request)
    return f'Booking for user id: {args}'


@app.route('/api/hotels_delete', methods=['DELETE'])
def delete_booking():
    """Delete booking."""
    args = validate_args(request)
    return f'Boking deleted with args: {args}'
