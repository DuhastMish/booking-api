"""Main application module."""
from flask import Flask
from flask_caching import Cache

from booking_api.argparser import booking_api_configuration
from booking_api.local_storage_manager import LocalStorage

local_storage_manager = LocalStorage()

app = Flask(__name__)

args = booking_api_configuration.parse_known_args()[0]

app.config.from_object('SETTINGS.Redis')

if args.debug:
    app.config.from_object('SETTINGS.Config')
else:
    app.config.from_object('SETTINGS.ProductionConfig')

cache = Cache(app, config=app.config)

from booking_api import api_handlers  # noqa: F401
