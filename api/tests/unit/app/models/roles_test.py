from app.models.roles import Roles


def test_roles():
    assert Roles.BASIC_ROLE == "basic"
    assert Roles.ADMIN_ROLE == "admin"
