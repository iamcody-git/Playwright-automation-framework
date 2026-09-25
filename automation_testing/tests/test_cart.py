import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
def test_cart_page_shows_added_item(page, cart_page):
    expect(cart_page.title).to_have_text("Your Cart")
    expect(cart_page.cart_items).to_have_count(1)
    assert "Sauce Labs Backpack" in cart_page.get_item_names()


def test_remove_item_from_cart_page(page, cart_page, inventory_page):
    cart_page.remove_item_by_name("Sauce Labs Backpack")

    expect(cart_page.cart_items).to_have_count(0)
    expect(inventory_page.cart_badge).to_be_hidden()


def test_continue_shopping_returns_to_products(page, cart_page):
    cart_page.click_continue_shopping()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


def test_checkout_button_goes_to_checkout_step_one(page, cart_page):
    cart_page.click_checkout()

    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")


def test_cart_is_empty_by_default(page, inventory_page):
    inventory_page.go_to_cart()
    cart = CartPageLocal(page)

    expect(cart.cart_items).to_have_count(0)


class CartPageLocal:
    """Small helper so the empty-cart test doesn't need the cart_page fixture (which adds an item)."""
    def __init__(self, page):
        self.cart_items = page.locator(".cart_item")