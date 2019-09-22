from app import db
from flask_login import UserMixin


class User(db.Model, UserMixin):  # type: ignore
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String)
    role = db.Column(db.String, nullable=False, unique=False)
