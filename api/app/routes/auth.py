from flask import Blueprint
from flask_apispec import marshal_with
from flask_apispec import use_kwargs
from marshmallow import Schema
from webargs import fields
from app.models.user import User

blueprint = Blueprint("authorization", __name__)


class SignupSchema(Schema):
    class Meta:
        fields = ("username", "password", "email_address")


class Signup:
    def __init__(self, username: str, password: str, email_address: str) -> None:
        self.username = username
        self.password = password
        self.email_address = email_address


@blueprint.route('/login')
def login():
    return 'Login'


@blueprint.route('/signup', methods=['GET'])
@use_kwargs(SignupSchema)
# @marshal_with(SignupSchema(many=True))
def signup(**kwargs):
    signup = Signup(**kwargs)
    user = User.query.filter_by(email_address=signup.email_address).first()
    print(user)
    return f"signup {signup.username}"



@blueprint.route('/logout')
def logout():
    return 'Logout'


@blueprint.route('/reset')
def reset():
    # Used to reset password
    return "reset"
