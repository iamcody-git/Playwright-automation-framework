from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.cart_items = page.locator(".cart_item")
        self.item_names = page.locator(".inventory_item_name")
        self.checkout_button = page.locator("[data-test='checkout']")
        self.continue_shopping_button = page.locator("[data-test='continue-shopping']")

    def get_item_names(self):
        return self.item_names.all_inner_texts()

    def remove_item_by_name(self, item_name):
        item = self.page.locator(".cart_item", has_text=item_name)
        item.locator("button", has_text="Remove").click()

    def click_checkout(self):
        self.checkout_button.click()

    def click_continue_shopping(self):
        self.continue_shopping_button.click()