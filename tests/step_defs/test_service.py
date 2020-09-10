import random

import requests
from faker import Faker
from pytest_bdd import given, when, then

fake = Faker()


#
# @scenario('../features/service.feature', 'Create new service')
# def test_create_service():
#     pass


@given("API endpoint for services")
def services_api():
    SERVICES_API = "http://localhost:8000/services"
    return SERVICES_API


@when("Data to create service a new service are set")
def step_impl():
    global service_data
    service_data = {
        'user_id': 1,
        'category_id': 1,
        'subcategory_id': 1,
        'name': fake.name(),
        'image': f"{fake.name()}.jpg",
        'price': random.randint(0, 10),
        'description': fake.name(),
        'username': fake.name()
    }


@when("User makes a post request to services endpoint with authentication headers")
def set_service_data(services_api, user_logged_in):
    global req
    files = {'image': open('./minion.jpg', 'rb')}

    req = requests.post(
        services_api, data=service_data, files=files, headers=user_logged_in
    )


@then("The response status code should be 200")
def create_status_code():
    assert req.status_code == 200


@then("Message should be Successfully created Service!")
def step_impl():
    message = req.json()['message']
    assert message == 'Successfully created Service!'


@then("Response should contain Service key")
def step_impl():
    req_json = req.json()
    assert 'Service' in req_json
