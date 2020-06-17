import requests
from pytest_bdd import when, then, scenarios

CONVERTERS = {
    'email': str,
    'password': str,
    'full_name': str,
    'status_code': int,
    'username':str
}

scenarios('../features/register_outline.feature', example_converters=CONVERTERS)


@when('Required data for registration are set "<email>","<password>","<full_name>,<username>"')
def specify_data(email, password, full_name,username):
    global data_to_register
    data_to_register = {
        'email': email,
        'password': password,
        'password_confirmation': password,
        'name': full_name,
        'username': username
    }


@when("POST request is made to endpoint with given data")
def post_req(api_endpoint):
    global res
    res = requests.post(
        api_endpoint, json=data_to_register
    )


@then('Response status code should be "<status_code>"')
def res_code(status_code):
    assert res.status_code == status_code
