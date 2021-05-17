from booking_api.constants import SQL_STRING

redis_url = 'redis://:p1b0a30407c1aa1ce6f23b3a89d5bdb643548caf501acc3e89b607adbd943f563@'\
            'ec2-54-228-38-233.eu-west-1.compute.amazonaws.com:8569'


class Redis(object):  # noqa: D101, D100
    CACHE_TYPE = 'RedisCache'
    CACHE_REDIS_URL = redis_url
    CACHE_DEFAULT_TIMEOUT = 5
    CACHE_DEFAULT_TIMOUT_DB = 5


class Celery(object):  # noqa: D101, D100
    CELERY_BROKER_URL = redis_url
    CELERY_BACKEND = 'db+' + SQL_STRING


class Config(object):  # noqa: D101, D100
    DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = 'hardcode'
    FLASK_SECRET = SECRET_KEY


class ProductionConfig(Config):  # noqa: D101
    DEVELOPMENT = False
    DEBUG = False
