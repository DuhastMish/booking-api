redis_url = 'redis://localhost:6379/0'


class Redis(object):  # noqa: D101, D100
    CACHE_TYPE = 'RedisCache'
    CACHE_REDIS_URL = redis_url
    CACHE_DEFAULT_TIMEOUT = 5
    CACHE_DEFAULT_TIMOUT_DB = 5


class Celery(object):  # noqa: D101, D100
    CELERY_BROKER_URL = redis_url
    CELERY_RESULT_BACKEND = redis_url


class Config(object):  # noqa: D101, D100
    DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = 'hardcode'
    FLASK_SECRET = SECRET_KEY


class ProductionConfig(Config):  # noqa: D101
    DEVELOPMENT = False
    DEBUG = False
