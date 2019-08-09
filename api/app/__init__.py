import os

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from app.routes import hello
from flask import Flask
from flask_apispec.extension import FlaskApiSpec
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # sqlalchemy db setup
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()

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
