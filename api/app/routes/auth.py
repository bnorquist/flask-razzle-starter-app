import logging

from app import db
from app.models.account_actions import AccountManager
from app.models.user import User
from flask import Blueprint
from flask_apispec import marshal_with
from flask_apispec import use_kwargs
from flask_login import login_user
from marshmallow import Schema
from webargs import fields
from werkzeug.security import check_password_hash


blueprint = Blueprint("authorization", __name__)


class LoginSchema(Schema):
    password = fields.Str(required=True)
    email = fields.Str(required=True)

    class Meta:
        strict = True


class Login(object):
    def __init__(self, password: str, email: str) -> None:
        self.password = password
        self.email = email


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

    user = User.query.filter_by(email=user_login.email).first()

    logging.info("User attempting to login")

    if not user:
        return AuthResponse("Username is not registered"), 404

    if not check_password_hash(user.password, user_login.password):
        return AuthResponse("Incorrect password"), 404

    login_user(user)
    return AuthResponse(message="logged in"), 200


@blueprint.route("/signup", methods=["POST"])
@use_kwargs(LoginSchema)
@marshal_with(AuthResponseSchema)
def signup(**kwargs):
    signup = Login(**kwargs)
    user = User.query.filter_by(email=signup.email).first()

    if user is not None:
        return (
            AuthResponse(message="An account with this email address already exists!"),
            400,
        )

    AccountManager.create_user(db, signup.email, signup.password)

    return AuthResponse(message="Your account has been created, welcome!"), 200


@blueprint.route("/logout")
def logout():
    return "Logout"


@blueprint.route("/reset")
def reset():
    # Used to reset password
    return "reset"
