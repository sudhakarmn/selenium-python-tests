from pages.login_page import LoginPage
from utils.config import LOGIN_URL

def test_login_wrong_password(browser_context):
    page = browser_context
    login = LoginPage(page)

    page.goto(LOGIN_URL)
    login.login("student", "wrongPassword")

    assert page.locator("text=Your password is invalid!").first.is_visible()
