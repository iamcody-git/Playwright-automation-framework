import json
from pathlib import Path
from pages.login_page import LoginPage

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