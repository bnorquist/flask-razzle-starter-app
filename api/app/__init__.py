import logging
import os

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from app.models.flask_config import DevelopmentConfig
from app.models.flask_config import ProductionConfig
from flask import Flask
from flask_apispec.extension import FlaskApiSpec
from flask_cors import CORS
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

logging.basicConfig(
    filename="logs/api.log", level=logging.INFO, format="%(asctime)s %(message)s"
)
logging.info("Init starting...")


db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    is_production = os.environ.get("ENVIRONMENT") == "PRODUCTION"
    if is_production:
        config = ProductionConfig()
    else:
        config = DevelopmentConfig()
        # initialize dev database here?

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    CORS(app)
    app.config.from_object(config)

    # sqlalchemy db setup
    app.config["SQLALCHEMY_DATABASE_URI"] = config.DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    # register blueprints
    from app.routes import hello
    from app.routes import auth

    app.register_blueprint(hello.blueprint)
    app.register_blueprint(auth.blueprint)

    # initialize flask login
    login_manager.init_app(app)

    # apispec
    app.config.update(
        {
            "APISPEC_SPEC": APISpec(
                title="savegroup",
                version="v1",
                plugins=[MarshmallowPlugin()],
                openapi_version="3.0.2",
            ),
            "APISPEC_SWAGGER_URL": "/swagger/",
        }
    )

    # swagger docs
    docs = FlaskApiSpec(app)
    docs.register(hello.hello, blueprint="hello_page")

    # create all tables
    if is_production:
        db.create_all()

    logging.info("app created")
    return app


app = create_app()

if __name__ == "__main__":
    app.run()
