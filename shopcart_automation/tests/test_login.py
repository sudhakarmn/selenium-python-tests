from pages.login_page import LoginPage
from utilities.read_config import ReadConfig

def test_valid_login(setup):
    driver = setup
    driver.get(ReadConfig.get_base_url())

    login = LoginPage(driver)
    login.login(ReadConfig.get_username(), ReadConfig.get_password())

    assert "inventory" in driver.current_url
