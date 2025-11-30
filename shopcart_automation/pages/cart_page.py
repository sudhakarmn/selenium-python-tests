from selenium.webdriver.common.by import By
from utilities.base import BasePage

class CartPage(BasePage):
    CHECKOUT_BTN = (By.ID, "checkout")

    def checkout(self):
        self.click(self.CHECKOUT_BTN)
