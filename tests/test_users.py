# tests/test_users.py

from utils.api_client import get
from utils.schema_validator import validate_schema

def test_get_all_users_status_code():
    response = get("users")
    assert response.status_code == 200

def test_user_fields_exist():
    user = get("users").json()[0]
    assert "id" in user
    assert "email" in user
    assert "username" in user
    assert "address" in user

def test_validate_user_schema():
    user = get("users/1").json()
    validate_schema(user, "data/schemas/user_schema.json")
