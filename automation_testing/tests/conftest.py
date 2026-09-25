import json
from pathlib import Path
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

import pytest

DATA_FILE = Path(__file__).resolve().parent.parent / "test_data" / "users.json"


@pytest.fixture(scope="session")
def test_data():
    """Load users and checkout details from users.json."""
    with open(DATA_FILE) as file:
        return json.load(file)

@pytest.fixture
def login_page(page):
    """Open the login page and return the LoginPage object."""
    login = LoginPage(page)
    login.open()
    return login

@pytest.fixture
def inventory_page(login_page, test_data):
    """Log in as standard_user and return the InventoryPage object."""
    login_page.login(test_data["users"]["standard"], test_data["password"])
    return InventoryPage(login_page.page)

@pytest.fixture
def cart_page(inventory_page):
    """Add one item, go to cart, and return the CartPage object."""
    inventory_page.add_item_to_cart_by_name("Sauce Labs Backpack")
    inventory_page.go_to_cart()
    return CartPage(inventory_page.page)

@pytest.fixture
def checkout_page(cart_page):
    """Go from cart to checkout step one and return the CheckoutPage object."""
    cart_page.click_checkout()
    return CheckoutPage(cart_page.page)