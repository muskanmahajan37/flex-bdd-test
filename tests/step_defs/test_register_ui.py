import time

from pytest_bdd import scenario, given, when, then, scenarios

scenarios('../features/ui/register_ui.feature')


@when("User clicks Sign Up")
def signup(browser):
    join_button = browser.find_element_by_class_name("register-link")
    time.sleep(1)
    join_button.click()

@then("Types name,username,email,password,and confirm password")
def send_data(browser):
    name="Valon Januzaj"
    username="vjanz"
    email="Vjanz@gmail.com"
    password="123123"
    confirm_password="123123"

    name_field = browser.find_element_by_name("name")
    username_field = browser.find_element_by_name("username")
    email_field = browser.find_element_by_name("email")
    password_field = browser.find_element_by_name("password")
    password_confirm_field = browser.find_element_by_name("confirmPassword")

    name_field.send_keys(name)
    username_field.send_keys(username)
    email_field.send_keys(email)
    password_field.send_keys(password)
    password_confirm_field.send_keys(confirm_password)
    time.sleep(3)

@then("User clicks submit button")
def step_impl(browser):
    browser.find_element_by_class_name("register-button").click()
    time.sleep(10)
