import pytest
from app.models.user import User
from tests.test_utils import TEST_EMAIL
from tests.test_utils import TEST_PASSWORD
from werkzeug.security import check_password_hash


class TestUser(object):
    @pytest.mark.parametrize(
        argnames=("email", "user_exists"),
        argvalues=[("123@xyz.com", False), (TEST_EMAIL, True)],
    )
    def test_get_user(self, email, user_exists, app_context):
        user = User.query.filter_by(email=email).first()

        if user_exists:
            assert user.email == TEST_EMAIL
            assert check_password_hash(user.password, TEST_PASSWORD) is True
        else:
            assert user is None
