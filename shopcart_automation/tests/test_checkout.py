from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utilities.read_config import ReadConfig

def test_checkout_flow(setup):
    driver = setup
    driver.get(ReadConfig.get_base_url())

    LoginPage(driver).login(ReadConfig.get_username(), ReadConfig.get_password())
    HomePage(driver).select_first_product()
    ProductPage(driver).add_to_cart()
    ProductPage(driver).go_to_cart()
    CartPage(driver).checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_details()
    checkout.finish_order()

    assert checkout.get_text(CheckoutPage.SUCCESS_MSG) == "Thank you for your order!"
