import os

class DevelopmentConfig(object):
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DB_FILENAME = os.getenv('DB_FILENAME')
    DB_PATH = os.getenv('DATABASE_URL')

    AUTH0_DOMAIN = os.getenv('AUTH0_DOMAIN')
    ALGORITHMS = os.getenv('ALGORITHMS')
    API_AUDIENCE = os.getenv('API_AUDIENCE')