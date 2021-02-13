from flask import Flask

from api_site.argparser import api_site_configuration
from api_site.local_storage_manager import LocalStorage

local_storage_manager = LocalStorage()

app = Flask(__name__)
args = api_site_configuration.parse_known_args()[0]

if args.debug:
    app.config.from_object('SETTINGS.Config')
else:
    app.config.from_object('SETTINGS.ProductionConfig')

from api_site import handlers  # noqa
