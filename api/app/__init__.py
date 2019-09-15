import os

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from app.models.flask_config import DevelopmentConfig
from app.models.flask_config import ProductionConfig
from app.routes import hello
from flask import Flask
from flask-cors imports CORS
from flask_apispec.extension import FlaskApiSpec
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    if os.environ.get("environment") == "production":
        config = ProductionConfig()
    else:
        config = DevelopmentConfig()
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    CORS(app)
    app.config.from_object(config)

    # sqlalchemy db setup
    app.config["SQLALCHEMY_DATABASE_URI"] = config.DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    # this needs to be called sometime before you interact with the database
    # with app.app_context():
    #     db.create_all()

    # register blueprints
    app.register_blueprint(hello.blueprint)

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

    return app


app = create_app()

if __name__ == "__main__":
    app.run()
