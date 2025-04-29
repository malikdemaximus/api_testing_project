# tests/test_products.py

from utils.api_client import get

def test_get_all_products_status_code():
    response = get("products")
    assert response.status_code == 200

def test_first_product_has_required_fields():
    response = get("products")
    product = response.json()[0]
    assert "id" in product
    assert "title" in product
    assert "price" in product
    assert "category" in product
