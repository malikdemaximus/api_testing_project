# tests/test_cart.py

from utils.api_client import get
 
def test_get_all_carts_status_code():
    response = get("carts")
    assert response.status_code == 200

def test_cart_contains_products():
    response = get("carts")
    cart = response.json()[0]
    assert "products" in cart
    assert isinstance(cart["products"], list)
