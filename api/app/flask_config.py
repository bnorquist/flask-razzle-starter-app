import os

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin


class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = os.environ.get("DATABASE_URL")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    APISPEC_SPEC = APISpec(
        title="savegroup",
        version="v1",
        plugins=[MarshmallowPlugin()],
        openapi_version="3.0.2",
    )
    APISPEC_SWAGGER_URL = "/swagger/"


class ProductionConfig(Config):
    pass


class StagingConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


ENV_CONFIG = {
    "production": ProductionConfig,
    "staging": StagingConfig,
    "development": DevelopmentConfig,
}
