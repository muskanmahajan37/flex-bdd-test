import requests
from faker import Faker
from pytest_bdd import scenario, given, when, then

from .conftest import BDD_BASE_URL

fake = Faker()


@scenario("../features/category.feature", "Add new Category")
def test_categories():
    pass


@given("API endpoint for categories")
def categories_endpoint():
    CATEGORIES_ENDPOINT = f"{BDD_BASE_URL}/categories"
    return CATEGORIES_ENDPOINT


@given("User is logged in")
def user_logged_in():
    data = {
        "email": "user@test.com",
        "password": "12345"
    }

    r = requests.post(
        f"{BDD_BASE_URL}/login/", data=data
    )
    tokens = r.json()
    access_token = tokens["access_token"]
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    print(headers)
    print(r.status_code)
    return headers


@when("POST request is made to endpoint with data and access token")
def post_request(categories_endpoint, user_logged_in):
    categories_data = {
        "name": fake.name(),
        "description": fake.name()
    }

    global req_categories
    req_categories = requests.post(
        "http://localhost:8000/categories", json=categories_data, headers=user_logged_in
    )
    res_json = req_categories.json()
    print(res_json)


@then("Response status should be 200")
def status_code():
    assert req_categories.status_code == 200
