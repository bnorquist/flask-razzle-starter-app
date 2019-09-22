from tests.test_utils import TEST_EMAIL
from tests.test_utils import TEST_PASSWORD


class TestAuth(object):
    def test_login(self, test_client):
        resp = test_client.get(
            f"/login?email_address={TEST_EMAIL}&password={TEST_PASSWORD}"
        )
        assert resp.status_code == 200

    def test_login_fail(self, test_client):
        resp = test_client.get(
            f"/login?email_address=abc@123.com&password=wrong_password"
        )
        assert resp.status_code == 404
