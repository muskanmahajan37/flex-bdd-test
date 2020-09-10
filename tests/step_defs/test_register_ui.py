import time
from typing import List, Any, Union

from faker import Faker
from pytest_bdd import when, then, scenarios, given, parsers

from tests.step_defs.conftest import SIGNUP_URL

fake = Faker()

scenarios('../features/ui/register_ui.feature')
STR_EXTRA = {
    "String": str
}
fake_password = fake.name()


@given("the user is on register page")
def step_impl(browser):
    browser.get(SIGNUP_URL)


@when(parsers.cfparse(
    'the user enters name "{name:String}" ,username "{username:String}" ,email "{email:String}",password "{password:String}" ,and confirm password "{password_confirm:String}"',
    extra_types=STR_EXTRA))
def send_data(browser, name, username, email, password,
              password_confirm):
    name_field = browser.find_element_by_name("name")
    username_field = browser.find_element_by_name("username")
    email_field = browser.find_element_by_name("email")
    password_field = browser.find_element_by_name("password")
    password_confirm_field = browser.find_element_by_name("confirmPassword")

    name_field.send_keys(fake.name())
    username_field.send_keys(fake.name())
    email_field.send_keys(fake.email())
    password_field.send_keys(fake_password)
    password_confirm_field.send_keys(fake_password)
    time.sleep(3)
    browser.find_element_by_class_name("register-button").click()
    time.sleep(5)  # Wait to show homescreen


@then("User account should be created, and user should be redirected to home page")
def home_screen(browser):
    current_url: Union[Union[int, List[Union[int, str]]], Any] = browser.current_url
    assert current_url == "http://localhost:3000/"  # Assert that user is already registered and in home page..
    time.sleep(2)


@when("the user leaves all the fields blank")
def empty_fields(browser):
    name_field = browser.find_element_by_name("name")
    username_field = browser.find_element_by_name("username")
    email_field = browser.find_element_by_name("email")
    password_field = browser.find_element_by_name("password")
    password_confirm_field = browser.find_element_by_name("confirmPassword")
    empty_str = ""

    name_field.send_keys(empty_str)
    username_field.send_keys(empty_str)
    email_field.send_keys(empty_str)
    password_field.send_keys(empty_str)
    password_confirm_field.send_keys(empty_str)
    time.sleep(3)
    browser.find_element_by_class_name("register-button").click()
    time.sleep(5)  # Wait to show homescreen


@then(parsers.cfparse('All the fields should show error message "{message:String}"', extra_types=STR_EXTRA))
def errors_assertion(browser, message):
    time.sleep(1)
    # The error messages are a list now because many fields are blank and they all have same class
    all_error_messages = browser.find_elements_by_class_name("error-message")
    length_of_array_excepted = 5

    assert len(all_error_messages) == length_of_array_excepted

    for error_msg in all_error_messages:
        assert error_msg.text == message


@when(parsers.cfparse('the user enters short username "{username:String}"', extra_types=STR_EXTRA))
def bad_username_entered(browser, username):
    name_field = browser.find_element_by_name("name")
    username_field = browser.find_element_by_name("username")
    email_field = browser.find_element_by_name("email")
    password_field = browser.find_element_by_name("password")
    password_confirm_field = browser.find_element_by_name("confirmPassword")

    name_field.send_keys(fake.name())
    username_field.send_keys(username)
    email_field.send_keys(fake.email())
    password_field.send_keys(fake_password)
    password_confirm_field.send_keys(fake_password)
    time.sleep(3)
    browser.find_element_by_class_name("register-button").click()
    time.sleep(5)  # Wait to show message


@then(parsers.cfparse('the user should see error "{message:String}', extra_types=STR_EXTRA))
def error_msg_returned(browser, message):
    time.sleep(1)
    # The error messages are a list now because many fields are blank and they all have same class
    error_messages = browser.find_elements_by_class_name("error-message")
    length_of_array_excepted = 1

    assert len(error_messages) == length_of_array_excepted

    assert error_messages[0].text == message
