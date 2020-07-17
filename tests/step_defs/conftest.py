import os

import pytest
import requests
import selenium.webdriver
from pytest_bdd import given


BDD_BASE_URL = os.getenv("BDD_BASE_URL")
SUPERUSER_EMAIL = os.getenv("SUPERUSER_EMAIL")
SUPERUSER_PASSWORD = os.getenv("SUPERUSER_PASSWORD")

# UI Test

@pytest.fixture
def browser():
    b = selenium.webdriver.Chrome(executable_path="resources/chromedriver.exe")
    b.implicitly_wait(10)
    b.maximize_window()
    yield b
    b.quit()

@given("API endpoint for flex-homepage is given")
def homepage_api():
    FLEX_HOME = "http://localhost:3000/"
    return FLEX_HOME


@given("FLEX homepage is shown")
def flex_homepage(homepage_api, browser):
    browser.get(homepage_api)


# Fixtures and given steps from other API tests
@given("API endpoint for user registration")
def api_endpoint() -> str:
    REGISTER_URL = f"{BDD_BASE_URL}/register"
    return REGISTER_URL


@given("API endpoint for user login")
def login_api_url():
    LOGIN_API_ENDPOINT = f"{BDD_BASE_URL}/login/"
    return LOGIN_API_ENDPOINT


@given("API endpoint for categories")
def categories_endpoint():
    CATEGORIES_ENDPOINT = f"{BDD_BASE_URL}/categories"
    return CATEGORIES_ENDPOINT



@given("User is logged in")
def user_logged_in():
    data = {
        "email": SUPERUSER_EMAIL,
        "password": SUPERUSER_PASSWORD
    }

    r = requests.post(
        f"{BDD_BASE_URL}/login/", data=data
    )
    tokens = r.json()
    access_token = tokens["access_token"]
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    return headers




