# tests/test_products.py

from utils.api_client import get
from utils.schema_validator import validate_schema

def test_get_all_products_status_code():
    response = get("products")
    assert response.status_code == 200

def test_validate_product_schema():
    response = get("products/1")
    validate_schema(response.json(), "data/schemas/product_schema.json")
