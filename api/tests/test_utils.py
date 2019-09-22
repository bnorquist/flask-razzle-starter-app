from app import app
from app import db
from app.models.user import User
from werkzeug.security import generate_password_hash


TEST_EMAIL = "test@test.com"
TEST_PASSWORD = "abcd"


def with_app_context(func):
    def wrapper():
        with app.app_context():
            return func()

    return wrapper


@with_app_context
def init_db():
    # this needs to be called sometime before you interact with the database
    db.drop_all()
    db.create_all()


@with_app_context
def seed_db():
    new_user = User(
        email_address=TEST_EMAIL,
        password=generate_password_hash(TEST_PASSWORD, method="sha256"),
        role="admin",
    )
    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
