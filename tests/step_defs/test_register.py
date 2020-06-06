import requests
from faker import Faker
from pytest_bdd import when, then, scenario

fake = Faker()
from .conftest import BDD_BASE_URL


@scenario("../features/register.feature", "User Registration with correct credentials")
def test_register_with_right_credentials():
    pass


@when("Required data for registration are set")
def required_data() -> None:
    password = fake.password()
    global registration_data
    registration_data = {
        "name": fake.name(),
        "email": fake.email(),
        "username": fake.name(),
        "password": password,
        "password_confirmation": password
    }


@when('POST request is made to endpoint with specified data')
def post_to_endpoint(api_endpoint) -> None:
    # making the request
    global request
    request = requests.post(
        f"{BDD_BASE_URL}/register", data=registration_data
    )


@then("Response status code should be 200")
def response_code() -> None:
    response = request
    response_json = request.json()
    assert response.status_code == 201


@then("The response body should contain id, email and hashed_password")
def request_body() -> None:
    pass
