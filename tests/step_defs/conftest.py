import os

import requests
from pytest_bdd import given

BDD_BASE_URL = os.getenv("BDD_BASE_URL")
SUPERUSER_EMAIL = os.getenv("SUPERUSER_EMAIL")
SUPERUSER_PASSWORD = os.getenv("SUPERUSER_PASSWORD")

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

