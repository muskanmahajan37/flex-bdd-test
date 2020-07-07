import time

from pytest_bdd import given, when, then, scenarios

scenarios('../features/ui/login_ui.feature')




@when("User clicks login")
def login(browser):
    login_elem = browser.find_element_by_id("login")
    time.sleep(3)
    login_elem.click()


@then("Types username and password")
def enter_data(browser):
    username = "admin@test.com"
    password="12345"
    email_field = browser.find_element_by_name("email")
    password_field = browser.find_element_by_name("password")

    email_field.send_keys(username)
    password_field.send_keys(password)
    time.sleep(3)
    submit_button = browser.find_element_by_class_name("login-button")
    submit_button.click()
    time.sleep(3)

@then("User should see homepage")
def see_results():
    pass
