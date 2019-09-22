import logging

from app import db
from app.models.roles import Roles
from app.models.user import User
from flask import Blueprint
from flask_apispec import marshal_with
from flask_apispec import use_kwargs
from flask_login import login_user
from marshmallow import Schema
from webargs import fields
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash


blueprint = Blueprint("authorization", __name__)


class LoginSchema(Schema):
    password = fields.Str(required=True)
    email_address = fields.Str(required=True)

    class Meta:
        strict = True


class Login(object):
    def __init__(self, password: str, email_address: str) -> None:
        self.password = password
        self.email_address = email_address


class AuthResponseSchema(Schema):
    message = fields.Str()


class AuthResponse(object):
    def __init__(self, message: str) -> None:
        self.message = message


@blueprint.route("/login", methods=["GET"])
@use_kwargs(LoginSchema, apply=True)
@marshal_with(AuthResponseSchema)
def login(**kwargs):
    user_login = Login(**kwargs)

    user = User.query.filter_by(email_address=user_login.email_address).first()

    logging.info("User attempting to login")

    if not user or not check_password_hash(user.password, user_login.password):
        return AuthResponse("Username or Password was incorrect"), 404

    login_user(user)
    return AuthResponse(message="logged in"), 200


@blueprint.route("/signup", methods=["POST"])
@use_kwargs(LoginSchema)
@marshal_with(AuthResponseSchema)
def signup(**kwargs):
    signup = Login(**kwargs)
    user = User.query.filter_by(email_address=signup.email_address).first()

    if user is not None:
        return (
            AuthResponse(message="An account with this email address already exists!"),
            400,
        )

    new_user = User(
        email_address=signup.email_address,
        role=Roles.BASIC_ROLE,
        password=generate_password_hash(password=signup.password),
    )
    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    return AuthResponse(message=f"Your account has been created, welcome!"), 200


@blueprint.route("/logout")
def logout():
    return "Logout"


@blueprint.route("/reset")
def reset():
    # Used to reset password
    return "reset"
