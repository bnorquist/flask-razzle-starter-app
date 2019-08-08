from app import db  # noqa
from app.services.postgres import create_user  # noqa


class TestPostgres:
    def test_create_user(self):
        # create_user("ben", "ben@example.com")
        # db.session()
        # these need to be run within the flask context i.e. with app.app_context(): ...
        pass
