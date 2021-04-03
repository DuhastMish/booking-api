class Config(object):  # noqa: D101, D100
    DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = 'hardcode'
    FLASK_SECRET = SECRET_KEY


class ProductionConfig(Config):  # noqa: D101
    DEVELOPMENT = False
    DEBUG = False
