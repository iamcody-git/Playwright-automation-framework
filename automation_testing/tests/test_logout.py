import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
def test_logout_returns_to_login_page(page, inventory_page):
    inventory_page.logout()

    expect(page).to_have_url("https://www.saucedemo.com/")
    expect(page.locator("#login-button")).to_be_visible()


def test_cannot_access_inventory_after_logout(page, inventory_page):
    inventory_page.logout()

    # Try to go straight to the inventory page without logging in again
    page.goto("/inventory.html")

    expect(page.locator("[data-test='error']")).to_contain_text("You can only access '/inventory.html' when you are logged in")