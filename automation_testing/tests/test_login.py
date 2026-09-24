import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
def test_login_with_valid_user(page, login_page, test_data):
    login_page.login(test_data["users"]["standard"], test_data["password"])

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")


def test_login_with_locked_out_user(login_page, test_data):
    login_page.login(test_data["users"]["locked_out"], test_data["password"])

    expect(login_page.error_message).to_contain_text("this user has been locked out")


def test_login_with_wrong_password(login_page, test_data):
    login_page.login(test_data["users"]["standard"], "wrong_password")

    expect(login_page.error_message).to_contain_text("do not match any user")


def test_login_with_empty_username(login_page, test_data):
    login_page.login("", test_data["password"])

    expect(login_page.error_message).to_contain_text("Username is required")


def test_login_with_empty_password(login_page, test_data):
    login_page.login(test_data["users"]["standard"], "")

    expect(login_page.error_message).to_contain_text("Password is required")