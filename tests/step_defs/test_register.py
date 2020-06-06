import requests
from faker import Faker
from pytest_bdd import when, then, scenario

fake = Faker()
from .conftest import BDD_BASE_URL


@scenario("../features/register.feature", "User Registration with correct credentials")
def test_register_with_right_credentials():
    pass


@scenario("../features/register.feature", "User Registration with wrong credentials")
def test_register_with_wrong_credentials():
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
        f"{BDD_BASE_URL}/register", json=registration_data
    )


@then("Response status code should be 200")
def response_code() -> None:
    response = request
    response_json = request.json()
    assert response.status_code == 201


@then("The response body should contain id, email and hashed_password")
def request_body() -> None:
    res_json = request.json()
    access_token = res_json["access_token"]
    assert "user" in res_json
    assert "name" in res_json["user"]
    assert res_json["user"]["image"] == "noimage.jpg"
    assert "access_token" in res_json
    assert len(access_token) > 20


@when("Data for registration don't fit the requirement fields")
def bad_data() -> None:
    global data
    data = {
        "name": fake.name(),
        "email": fake.email(),
        "username": fake.name(),
        "password": "",
        "password_confirmation": ""
    }


@when("POST request is made to endpoint with bad body request")
def request_with_bad_data(api_endpoint):
    global r
    r = requests.post(
        api_endpoint, json=data
    )
    return r


@then("Response status code should be 422")
def response_status_code() -> None:
    res_json: dict = r.json()
    assert r.status_code == 422
    assert res_json
    assert res_json['error']["password"][0] == "The password field is required."
