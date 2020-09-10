import time

from faker import Faker
from pytest_bdd import scenarios, given
from pytest_bdd import then
from selenium.webdriver.common.keys import Keys

from tests.step_defs.conftest import TEST_USER_EMAIL, TEST_USER_PASSWORD, LOGIN_URL

scenarios('../features/ui/order_ui.feature')

fake = Faker()


@given("user logs in their account")
def user_logged_in(browser):
    browser.get(LOGIN_URL)
    username = TEST_USER_EMAIL
    password = TEST_USER_PASSWORD
    email_field = browser.find_element_by_name("email")
    password_field = browser.find_element_by_name("password")
    time.sleep(5)
    email_field.send_keys(username)
    password_field.send_keys(password)
    submit_button = browser.find_elements_by_class_name("login-button")[0]
    time.sleep(3)
    submit_button.click()


@then("User navigates to programming")
def step_impl(browser):
    a_li = browser.find_elements_by_class_name("parent-li")
    elem = a_li[0]
    time.sleep(2)
    elem.click()


@then("User clicks on a service")
def step_impl(browser):
    services = browser.find_elements_by_class_name("service-container")
    first_service = services[0]
    first_service.send_keys(Keys.ENTER)
    time.sleep(2)


@then("Chooses to pay")
def enter_payment_data(browser):
    stripe_button = browser.find_elements_by_class_name('StripeCheckout')[0].click()
    time.sleep(3)
    # Switch the current frame to stripe_checkout_app frame
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
def finish_payment(browser):
    # the switch_to_default_content switches the screen from the modal, because the stripe form it's a modal
    # to enter those data and to connect them directly with the stripe api
    browser.switch_to.default_content()
    time.sleep(3)
