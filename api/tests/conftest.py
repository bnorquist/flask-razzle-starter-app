import os

import pytest
from app import app
from tests.test_utils import init_db
from tests.test_utils import seed_db

if os.environ.get("ENVIRONMENT") == "DEVELOPMENT":
    init_db()
    seed_db()


@pytest.fixture
def test_client():
    return app.test_client()


@pytest.fixture
def app_context():
    with app.app_context():
        yield
