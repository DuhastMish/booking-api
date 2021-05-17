from booking_api.app import app

# postgresql://username:password@localhost:5432/dbname
SQL_STRING = 'postgres://wwdhglocyynans:9e7337da111a9eaf88d24ea1524efa6e0ba50a4c383a33809cdffcec98a5fd27@'\
             'ec2-54-228-139-34.eu-west-1.compute.amazonaws.com:5432/d4iq8notnsdpiv'

CACHE_DEFAULT_TIMEOUT = app.config.get('CACHE_DEFAULT_TIMEOUT')
CACHE_DEFAULT_TIMOUT_DB = app.config.get('CACHE_DEFAULT_TIMOUT_DB')
