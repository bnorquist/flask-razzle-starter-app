import logging
import os

from app.flask_config import DevelopmentConfig
from app.flask_config import ENV_CONFIG
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
    environment = os.environ.get("ENVIRONMENT")
    config = ENV_CONFIG.get(environment, DevelopmentConfig)

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    CORS(app)
    app.config.from_object(config())

    db.init_app(app)

    # register blueprints
    from app.routes import hello
    from app.routes import auth

    app.register_blueprint(hello.blueprint)
    app.register_blueprint(auth.blueprint)

    # initialize flask login
    login_manager.init_app(app)

    # swagger docs
    docs = FlaskApiSpec(app)
    docs.register(hello.hello, blueprint="hello_page")

    logging.info("app created")
    return app


app = create_app()

if __name__ == "__main__":
    app.run()
