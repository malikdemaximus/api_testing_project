# tests/test_users.py

from utils.api_client import get
import pytest

def test_get_all_users_status_code():
    response = get("users")
    assert response.status_code == 200

def test_user_fields_exist():
    response = get("users")
    user = response.json()[0]
    assert "id" in user
    assert "email" in user
    assert "username" in user
    assert "address" in user
