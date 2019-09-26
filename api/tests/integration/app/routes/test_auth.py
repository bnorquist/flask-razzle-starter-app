from tests.test_utils import TEST_EMAIL
from tests.test_utils import TEST_PASSWORD


class TestAuth(object):
    def test_login(self, test_client):
        resp = test_client.get(f"/login?email={TEST_EMAIL}&password={TEST_PASSWORD}")
        assert resp.status_code == 200

    def test_login_fail(self, test_client):
        resp = test_client.get(f"/login?email=abc@123.com&password=wrong_password")
        assert resp.status_code == 404

    def test_signup(self, test_client):
        resp = test_client.post(
            "/signup", data={"email": "tb12@gmail.com", "password": "patriots"}
        )
        assert resp.status_code == 200
        assert resp.json == {"message": "Your account has been created, welcome!"}

    def test_signup_account_already_exists(self, test_client):
        resp = test_client.post(
            "/signup", data={"email": TEST_EMAIL, "password": TEST_PASSWORD}
        )
        assert resp.status_code == 400
        assert resp.json == {
            "message": "An account with this email address already exists!"
        }
