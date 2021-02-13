from flask import Flask

app = Flask(__name__)

app.config.from_object('SETTINGS.ProductionConfig')

from api_site import handlers  # noqa
