"""This module runs application."""
from booking_api.app import app


def main():
    """App run."""
    app.run('127.0.0.1', port='5001')
