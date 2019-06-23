from flask import Blueprint
from marshmallow import Schema
from flask_apispec import marshal_with, use_kwargs
from webargs import fields


blueprint = Blueprint('hello_page', __name__)


class PersonSchema(Schema):
    class Meta:
        fields = ['name']


class Person:
    def __init__(self, name):
        self.name = name


# a simple page that says hello
@blueprint.route('/api/hello')
@use_kwargs({'name': fields.Str()})
@marshal_with(PersonSchema)
def hello(**kwargs):
    return Person(**kwargs)
