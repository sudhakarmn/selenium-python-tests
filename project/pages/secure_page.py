from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SecurePage(BasePage):

    SUCCESS_MESSAGE = (By.TAG_NAME, "h1")

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)
