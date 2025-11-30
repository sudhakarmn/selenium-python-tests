from selenium.webdriver.common.by import By
from utilities.base import BasePage

class HomePage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    PRODUCT = (By.XPATH, "//div[@class='inventory_item_name '][1]")

    def select_first_product(self):
        self.click(self.PRODUCT)