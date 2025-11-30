from pages.login_page import LoginPage
from pages.home_page import HomePage
from utilities.read_config import ReadConfig

def test_product_list_visible(setup):
    driver = setup
    driver.get(ReadConfig.get_base_url())

    LoginPage(driver).login(ReadConfig.get_username(), ReadConfig.get_password())
    home = HomePage(driver)

    assert home.is_visible(HomePage.TITLE)
