import os


class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = os.environ.get("DATABASE_URL")


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
