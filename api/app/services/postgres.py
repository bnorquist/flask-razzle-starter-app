from app import db
from app.models.user import User


def create_user(email: str, role: str) -> None:
    u = User()
    u.email = email
    u.role = role
    db.session.add(u)
    db.session.commit()
