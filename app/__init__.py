# import os

from flask import Flask
from app.routes import hello
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # # ensure the instance folder exists
    # http://flask.pocoo.org/docs/1.0/tutorial/factory/
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    # register blueprints
    app.register_blueprint(hello.blueprint)

    # apispec
    app.config.update({
        'APISPEC_SPEC': APISpec(
            title='savegroup',
            version='v1',
            plugins=[MarshmallowPlugin()],
            openapi_version="3.0.2",
        ),
        'APISPEC_SWAGGER_URL': '/swagger/',
    })

    return app


app = create_app()

# swagger docs
docs = FlaskApiSpec(app)
docs.register(hello.hello, blueprint="hello_page")

if __name__ == '__main__':
    app.run()
