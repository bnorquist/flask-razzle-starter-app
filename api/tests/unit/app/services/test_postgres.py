from api.app.services import create_user


class TestPostgres:
    def test_create_user(self):
        create_user("ben", "ben@example.com")
        import pdb

        pdb.set_trace()
