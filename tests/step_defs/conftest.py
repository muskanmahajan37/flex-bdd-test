import os

from pytest_bdd import given

BDD_BASE_URL = os.getenv("BDD_BASE_URL")


@given("API endpoint for user registration")
def api_endpoint() -> str:
    REGISTER_URL = f"{BDD_BASE_URL}/register"
    return REGISTER_URL


@given("API endpoint for user login")
def login_api_url():
    LOGIN_API_ENDPOINT = f"{BDD_BASE_URL}/login/"
    return LOGIN_API_ENDPOINT
