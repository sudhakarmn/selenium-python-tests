from selenium.webdriver.common.by import By
from utilities.base import BasePage

class ProductPage(BasePage):
    ADD_TO_CART = (By.ID, "add-to-cart")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def add_to_cart(self):
        self.click(self.ADD_TO_CART)

    def go_to_cart(self):
        self.click(self.CART_ICON)