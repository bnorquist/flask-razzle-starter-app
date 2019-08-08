from api.app import db
from api.app.models.user import User


def create_user(username: str, email: str) -> None:
    u = User()
    u.username = username
    u.email = email
    db.session.add(u)
    db.session.commit()
