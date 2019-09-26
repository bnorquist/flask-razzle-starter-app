import os

import pytest
from app import app

if os.environ.get("FLASK_ENV") == "development":
    from tests.test_utils import init_db
    from tests.test_utils import seed_db

    init_db()
    seed_db()


@pytest.fixture
def test_client():
    return app.test_client()


@pytest.fixture
def app_context():
    with app.app_context():
        yield
