# import os

from flask import Flask
from app.routes import hello


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
    app.register_blueprint(hello.blueprint)

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
