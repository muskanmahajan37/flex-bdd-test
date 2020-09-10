import time

from pytest_bdd import given, when, then, scenarios, parsers

from tests.step_defs.conftest import LOGIN_URL

scenarios('../features/ui/login_ui.feature')


@given("the user is on login page")
def user_login_page(browser):
    browser.get(LOGIN_URL)


STR_EXTRA = {
    "String": str
}


@when(parsers.cfparse('the user enters email "{email:String}" and password "{password:String}"', extra_types=STR_EXTRA))
def data_input(browser, email, password):
    email_field = browser.find_element_by_name("email")
    password_field = browser.find_element_by_name("password")

    email_field.send_keys(email)
    password_field.send_keys(password)
    time.sleep(3)
    submit_button = browser.find_element_by_class_name("login-button")
    submit_button.click()
    time.sleep(3)


@then("User should see homepage dashboard")
def result_excepted():
    pass


@when(parsers.cfparse('the user tries to login with "{email:String}" and password "{password:String}',
                      extra_types=STR_EXTRA))
def step_impl(browser, email, password):
    email_field = browser.find_element_by_name("email")
    password_field = browser.find_element_by_name("password")

    email_field.send_keys(email)
    password_field.send_keys(password)
    time.sleep(3)
    submit_button = browser.find_element_by_class_name("login-button")
    submit_button.click()
    time.sleep(3)


@then(parsers.cfparse('User should see message "{message:String}"',
                      extra_types=STR_EXTRA))
def auth_failed(browser, message):
    time.sleep(1)
    error_msg = browser.find_elements_by_class_name("error-message")[0]
    assert error_msg.text == message


@when(parsers.cfparse('the user tries to login entering  email "{email:String}" and  password "{password:String}"',
                      extra_types=STR_EXTRA))
def bad_email_format(browser, email, password):
    email_field = browser.find_element_by_name("email")
    password_field = browser.find_element_by_name("password")

    email_field.send_keys(email)
    password_field.send_keys(password)
    time.sleep(3)
    submit_button = browser.find_element_by_class_name("login-button")
    submit_button.click()
    time.sleep(3)


@then(parsers.cfparse('User should see error message "{message:String}"', extra_types=STR_EXTRA))
def error_msg_email(browser, message):
    time.sleep(1)
    error_msg = browser.find_elements_by_class_name("error-message")[0]
    assert error_msg.text == message


@when("the user leaves email as blank and password as blank and clicks login")
def step_impl(browser):
    email_field = browser.find_element_by_name("email")
    password_field = browser.find_element_by_name("password")

    email_field.send_keys("")
    password_field.send_keys("")
    time.sleep(3)
    submit_button = browser.find_element_by_class_name("login-button")
    submit_button.click()
    time.sleep(3)


@then(parsers.cfparse('User should see error messages "{message:String}"', extra_types=STR_EXTRA))
def step_impl(browser, message):
    number_of_errors = browser.find_elements_by_class_name("error-message")
    assert len(number_of_errors) == 2

    first_error = number_of_errors[0]
    second_error = number_of_errors[1]

    assert first_error.text == message
    assert second_error.text == message
    time.sleep(1)
