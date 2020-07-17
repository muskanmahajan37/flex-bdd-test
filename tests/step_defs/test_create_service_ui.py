import time

from pytest_bdd import when, then, scenarios

scenarios('../features/ui/create_service_ui.feature')


@when("User clicks login")
def login(browser):
    login_elem = browser.find_element_by_id("login")
    time.sleep(3)
    login_elem.click()


@then("Types username and password")
def enter_data(browser):
    username = "admin@test.com"
    password = "12345"
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


@then("User clicks profile icon")
def click_profile(browser):
    profile_image = browser.find_elements_by_class_name("profile-image")[0]
    profile_image.click()


@then("Selects Profile")
def step_impl(browser):
    profile_menu = browser.find_elements_by_class_name("header-submenu-item")[0]
    profile_menu.click()


@then("Press Create Service button")
def step_impl(browser):
    profile_menu = browser.find_elements_by_tag_name("button")[0]
    profile_menu.click()


@then("Fill all the fields")
def step_impl(browser):
    name  = browser.find_element_by_name("name")
    price = browser.find_element_by_name("price")
    description = browser.find_element_by_id("formBasicDescription")
    image = browser.find_elements_by_class_name("form-control-file")[0]
    name.send_keys("PRODUKTI 1")
    price.send_keys(100)
    description.send_keys("Pershkrimi")
    image.click()



@then("Click create new service")
def step_impl():
    pass


@then("Service should be created")
def step_impl():
    pass
