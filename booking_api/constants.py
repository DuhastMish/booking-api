from booking_api.app import app

# postgresql://username:password@localhost:5432/dbname
SQL_STRING = 'postgresql://postgres:postgres@localhost:5432/booking_api'

CACHE_DEFAULT_TIMEOUT = app.config.get('CACHE_DEFAULT_TIMEOUT')
CACHE_DEFAULT_TIMOUT_DB = app.config.get('CACHE_DEFAULT_TIMOUT_DB')
