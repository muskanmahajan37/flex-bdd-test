import os
from pathlib import Path  # python3 only

import pytest
from dotenv import load_dotenv
from pytest_bdd import given, when, then, scenarios
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
scenarios('../features/web.feature')


# Fixtures
@pytest.fixture
def browser():
    b = webdriver.Chrome("resources/chromedriver.exe")
    b.implicitly_wait(10)
    yield b
    b.quit()


FACEBOOK = 'https://facebook.com/'


@given("the Facebook home page is displayed")
def facebook_home(browser):
    browser.get(FACEBOOK)


@when("the user enters username and password")
def step_impl(browser):
    username = browser.find_element_by_id("email")
    password = browser.find_element_by_id("pass")
    submit = browser.find_element_by_css_selector("[value=\"Log In\"]")
    username.send_keys("+38345519043")
    password.send_keys(os.getenv("FACEBOOK_PASSWORD") + Keys.RETURN)


@then("user should see facebook home page")
def fb_home(browser):
    browser.get(FACEBOOK)
