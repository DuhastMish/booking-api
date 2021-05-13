class Redis(object):  # noqa: D101, D100
    CACHE_TYPE = 'RedisCache'
    CACHE_REDIS_URL = 'redis://localhost:6379/0'
    CACHE_DEFAULT_TIMEOUT = 60
    CACHE_DEFAULT_TIMOUT_DB = 30


class Config(object):  # noqa: D101, D100
    DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = 'hardcode'
    FLASK_SECRET = SECRET_KEY


class ProductionConfig(Config):  # noqa: D101
    DEVELOPMENT = False
    DEBUG = False
