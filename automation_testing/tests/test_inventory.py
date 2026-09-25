import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
def test_inventory_page_loads_with_six_items(page, inventory_page):
    expect(inventory_page.title).to_have_text("Products")
    expect(inventory_page.inventory_items).to_have_count(6)


def test_sort_name_a_to_z(inventory_page):
    inventory_page.sort_by("az")
    names = inventory_page.get_item_names()

    assert names == sorted(names)


def test_sort_name_z_to_a(inventory_page):
    inventory_page.sort_by("za")
    names = inventory_page.get_item_names()

    assert names == sorted(names, reverse=True)


def test_sort_price_low_to_high(inventory_page):
    inventory_page.sort_by("lohi")
    prices = inventory_page.get_item_prices()

    assert prices == sorted(prices)


def test_sort_price_high_to_low(inventory_page):
    inventory_page.sort_by("hilo")
    prices = inventory_page.get_item_prices()

    assert prices == sorted(prices, reverse=True)


def test_add_single_item_to_cart(page, inventory_page):
    inventory_page.add_item_to_cart_by_name("Sauce Labs Backpack")

    expect(inventory_page.cart_badge).to_have_text("1")


def test_add_multiple_items_to_cart(page, inventory_page):
    inventory_page.add_item_to_cart_by_name("Sauce Labs Backpack")
    inventory_page.add_item_to_cart_by_name("Sauce Labs Bike Light")

    expect(inventory_page.cart_badge).to_have_text("2")


def test_remove_item_from_cart(page, inventory_page):
    inventory_page.add_item_to_cart_by_name("Sauce Labs Backpack")
    expect(inventory_page.cart_badge).to_have_text("1")

    inventory_page.remove_item_from_cart_by_name("Sauce Labs Backpack")
    expect(inventory_page.cart_badge).to_be_hidden()