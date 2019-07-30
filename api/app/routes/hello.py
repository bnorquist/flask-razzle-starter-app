from flask import Blueprint
from flask_apispec import marshal_with
from flask_apispec import use_kwargs
from marshmallow import Schema
from webargs import fields


blueprint = Blueprint("hello_page", __name__)


class PersonSchema(Schema):
    class Meta:
        fields = ["name"]


class Person:
    def __init__(self, name: str) -> None:
        self.name = name


# a simple page that says hello
@blueprint.route("/hello")
@use_kwargs({"name": fields.Str()})
@marshal_with(PersonSchema)
def hello(**kwargs):
    return Person(**kwargs)
