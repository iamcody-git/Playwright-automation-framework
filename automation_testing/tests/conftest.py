import json
from pathlib import Path
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

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