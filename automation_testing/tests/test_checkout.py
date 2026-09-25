import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
def test_checkout_step_one_loads(page, checkout_page):
    expect(checkout_page.title).to_have_text("Checkout: Your Information")


def test_checkout_with_valid_info_goes_to_overview(page, checkout_page, test_data):
    info = test_data["checkout_info"]
    checkout_page.fill_information(info["first_name"], info["last_name"], info["zip_code"])

    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
    expect(checkout_page.title).to_have_text("Checkout: Overview")


def test_checkout_missing_first_name_shows_error(page, checkout_page):
    checkout_page.fill_information("", "User", "12345")

    expect(checkout_page.error_message).to_contain_text("First Name is required")


def test_checkout_missing_last_name_shows_error(page, checkout_page):
    checkout_page.fill_information("Test", "", "12345")

    expect(checkout_page.error_message).to_contain_text("Last Name is required")


def test_checkout_missing_zip_code_shows_error(page, checkout_page):
    checkout_page.fill_information("Test", "User", "")

    expect(checkout_page.error_message).to_contain_text("Postal Code is required")


@pytest.mark.smoke
def test_full_checkout_flow_completes_order(page, checkout_page, test_data):
    info = test_data["checkout_info"]
    checkout_page.fill_information(info["first_name"], info["last_name"], info["zip_code"])

    expect(checkout_page.cart_items).to_have_count(1)

    checkout_page.finish_checkout()

    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
    expect(checkout_page.complete_header).to_have_text("Thank you for your order!")


def test_back_home_after_order_returns_to_products(page, checkout_page, test_data):
    info = test_data["checkout_info"]
    checkout_page.fill_information(info["first_name"], info["last_name"], info["zip_code"])
    checkout_page.finish_checkout()

    checkout_page.go_back_home()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")