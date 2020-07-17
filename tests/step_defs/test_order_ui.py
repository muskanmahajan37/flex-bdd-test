import time

from pytest_bdd import when, then, scenarios
from selenium.webdriver.common.keys import Keys

scenarios('../features/ui/order_ui.feature')
from faker import Faker
from pytest_bdd import given, when, then, scenario

fake = Faker()

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
    submit_button = browser.find_element_by_class_name("login-button")
    submit_button.click()


@then("User should see homepage")
def see_results():
    pass


@then("User navigates to programming")
def step_impl(browser):
    a_li = browser.find_elements_by_class_name("parent-li")
    elem = a_li[0]
    elem.click()


@then("User clicks on a service")
def step_impl(browser):
    services = browser.find_elements_by_class_name("service-container")
    first_service = services[0]
    first_service.send_keys(Keys.ENTER)


@then("Chooses to pay")
def step_impl(browser):
    stripe_button = browser.find_elements_by_class_name('StripeCheckout')[0].click()
    time.sleep(3)
    browser.switch_to.frame('stripe_checkout_app')
    browser.find_element_by_xpath("//input[@placeholder='Email']").send_keys(fake.email())
    time.sleep(0.5)
    card_input = browser.find_element_by_xpath("//input[@placeholder='Card number']")
    card_input.send_keys('4242')
    time.sleep(0.25)
    card_input.send_keys('4242')
    time.sleep(0.25)
    card_input.send_keys('4242')
    time.sleep(0.25)
    card_input.send_keys('4242')
    time.sleep(0.25)
    browser.find_element_by_xpath("//input[@placeholder='MM / YY']").send_keys("0121")
    time.sleep(0.5)
    browser.find_element_by_xpath("//input[@placeholder='CVC']").send_keys("121")
    time.sleep(0.5)
    browser.find_element_by_css_selector(".Checkbox-tick").click()
    time.sleep(2)
    browser.find_element_by_xpath("//input[@type='tel' and @value='+381 ']").send_keys(fake.phone_number())

    browser.find_element_by_tag_name("button").click()


@then("The payment should be finished")
def step_impl(browser):
    time.sleep(3)
    browser.switch_to.default_content()

