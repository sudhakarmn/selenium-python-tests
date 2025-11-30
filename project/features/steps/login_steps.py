from behave import given, when, then
from pages.login_page import LoginPage
from pages.secure_page import SecurePage


@given("I am on the login page")
def step_open_login(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open_login_page()


@when("I enter valid username and password")
def step_enter_credentials(context):
    context.login_page.login("student", "Password123")

@when("I click the login button")
def step_click_login(context):
    context.login_page.click_login()

@then("I should be redirected to the secure area")
def step_redirect(context):
    assert "logged-in-successfully" in context.driver.current_url


@then("I should see a success message")
def step_success(context):
    secure_page = SecurePage(context.driver)
    assert secure_page.get_success_message() == "Logged In Successfully"
