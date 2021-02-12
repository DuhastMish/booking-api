from . import app
from api_site.argparser import api_site_configuration


def main():
    args = api_site_configuration.parse_known_args()[0]

    app.run('0.0.0.0', port='5007', debug=args.debug)
