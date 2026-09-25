from playwright.sync_api import Page


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")

        # Step One: information form
        self.first_name_input = page.locator("[data-test='firstName']")
        self.last_name_input = page.locator("[data-test='lastName']")
        self.zip_code_input = page.locator("[data-test='postalCode']")
        self.continue_button = page.locator("[data-test='continue']")
        self.error_message = page.locator("[data-test='error']")

        # Step Two: overview
        self.cart_items = page.locator(".cart_item")
        self.item_total = page.locator(".summary_subtotal_label")
        self.tax = page.locator(".summary_tax_label")
        self.total = page.locator(".summary_total_label")
        self.finish_button = page.locator("[data-test='finish']")

        # Complete
        self.complete_header = page.locator(".complete-header")
        self.back_home_button = page.locator("[data-test='back-to-products']")

    def fill_information(self, first_name, last_name, zip_code):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.zip_code_input.fill(zip_code)
        self.continue_button.click()

    def finish_checkout(self):
        self.finish_button.click()

    def go_back_home(self):
        self.back_home_button.click()