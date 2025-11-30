from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://practicetestautomation.com/practice-test-login/"

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "submit")

    def open_login_page(self):
        self.open(self.URL)

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
    
    def click_login(self):
        self.click(self.LOGIN_BTN)


1.open URL
2.fill values
3. check for blank fields
4. check valid values
5. check invalid values
6. check forgot password
7. also verifi