from flask import Blueprint

blueprint = Blueprint('hello_page', __name__)


# a simple page that says hello
@blueprint.route('/hello')
def hello():
    return 'Hello, World!'
