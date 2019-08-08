from app import db
from app.models.user import User


def create_user(username: str, email: str, role: str) -> None:
    u = User()
    u.username = username
    u.email = email
    u.role = role
    db.session.add(u)
    db.session.commit()
