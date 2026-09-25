from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.sort_dropdown = page.locator("[data-test='product-sort-container']")
        self.inventory_items = page.locator(".inventory_item")
        self.item_names = page.locator(".inventory_item_name")
        self.item_prices = page.locator(".inventory_item_price")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")

        self.menu_button = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator("#logout_sidebar_link")

    def sort_by(self, option_value):
        """option_value: 'az', 'za', 'lohi', 'hilo'"""
        self.sort_dropdown.select_option(option_value)

    def get_item_names(self):
        return self.item_names.all_inner_texts()

    def get_item_prices(self):
        prices_text = self.item_prices.all_inner_texts()
        return [float(price.replace("$", "")) for price in prices_text]

    def add_item_to_cart_by_name(self, item_name):
        item = self.page.locator(".inventory_item", has_text=item_name)
        item.locator("button", has_text="Add to cart").click()

    def remove_item_from_cart_by_name(self, item_name):
        item = self.page.locator(".inventory_item", has_text=item_name)
        item.locator("button", has_text="Remove").click()

    def go_to_cart(self):
        self.cart_link.click()

    def logout(self):
        self.menu_button.click()
        self.logout_link.click()