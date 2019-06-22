from flask import Blueprint
from marshmallow import Schema
from flask_apispec import marshal_with
from webargs import fields
from webargs.flaskparser import use_args


blueprint = Blueprint('hello_page', __name__)


class PersonSchema(Schema):
    name = fields.Str()


# a simple page that says hello
@blueprint.route('/api/hello')
@use_args({'name': fields.Str()})
def hello(args):
    return f"Hello {args.get('name')}!"
