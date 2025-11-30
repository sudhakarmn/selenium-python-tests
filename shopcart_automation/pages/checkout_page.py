from selenium.webdriver.common.by import By
from utilities.base import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    SUCCESS_MSG = (By.CLASS_NAME, "complete-header")

    def fill_details(self):
        self.type(self.FIRST_NAME, "Sudhakara")
        self.type(self.LAST_NAME, "MN")
        self.type(self.ZIP, "560001")
        self.click(self.CONTINUE_BTN)

    def finish_order(self):
        self.click(self.FINISH_BTN)
