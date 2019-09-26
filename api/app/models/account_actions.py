from app.models.roles import Roles
from app.models.user import User
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash


class AccountManager(object):
    @staticmethod
    def create_user(
        db: SQLAlchemy, email: str, password: str, role: str = Roles.BASIC_ROLE
    ) -> None:
        password_hash = generate_password_hash(password=password)
        new_user = User(email=email, role=role, password=password_hash)
        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()
