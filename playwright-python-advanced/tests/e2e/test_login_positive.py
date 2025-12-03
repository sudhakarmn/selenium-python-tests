from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils.config import LOGIN_URL, USERNAME, PASSWORD

def test_login_positive(browser_context):
    page = browser_context
    login = LoginPage(page)
    home = HomePage(page)

    page.goto(LOGIN_URL)
    login.login(USERNAME, PASSWORD)

    assert home.is_logged_in(), "Login success message not visible"
