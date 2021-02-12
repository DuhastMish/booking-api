class Config(object):
    DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = 'hardcode'
    FLASK_SECRET = SECRET_KEY


class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False
