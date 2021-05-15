"""Main application module."""
from celery import Celery
from flask import Flask
from flask_caching import Cache

from booking_api.argparser import booking_api_configuration
from booking_api.local_storage_manager import LocalStorage

local_storage_manager = LocalStorage()

app = Flask(__name__)

args = booking_api_configuration.parse_known_args()[0]

app.config.from_object('SETTINGS.Redis')
app.config.from_object('SETTINGS.Celery')

if args.debug:
    app.config.from_object('SETTINGS.Config')
else:
    app.config.from_object('SETTINGS.ProductionConfig')

cache = Cache(app, config=app.config)

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])

from booking_api import api_handlers  # noqa: F401
