from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from utilities.read_config import ReadConfig

def test_add_to_cart(setup):
    driver = setup
    driver.get(ReadConfig.get_base_url())
    LoginPage(driver).login(ReadConfig.get_username(), ReadConfig.get_password())
    HomePage(driver).select_first_product()

    product = ProductPage(driver)
    product.add_to_cart()
    product.go_to_cart()

    assert "cart" in driver.current_url
