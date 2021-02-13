from flask import Flask

from api_site.argparser import api_site_configuration

app = Flask(__name__)
args = api_site_configuration.parse_known_args()[0]
# import pdb; pdb.set_trace()
if args.debug:
    app.config.from_object('SETTINGS.Config')
else:
    app.config.from_object('SETTINGS.ProductionConfig')

from api_site import handlers  # noqa
