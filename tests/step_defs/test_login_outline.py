import requests
from pytest_bdd import when, then, scenarios

CONVERTERS = {
    'email': str,
    'password': str,
    'status_code': int,
    'message': str,
}
scenarios('../features/login_outline.feature', example_converters=CONVERTERS)


@when('Required data for login are set "<email>","<password>"')
def data_for_login(email, password):
    global login_data
    global user_password
    user_password = password
    login_data = {
        "email": email,
        "password": password
    }


@then("POST request is made to endpoint with data provided")
def step_impl(login_api_url):
    global request_login
    request_login = requests.post(
        login_api_url, data=login_data
    )


@then('Response message should be "<message>" and status code "<status_code>"')
def status_code_response(message, status_code):
    res_js = request_login.json()
    err_msg = message
    assert request_login.status_code == status_code
    if status_code == 400:
        assert res_js["message"] == err_msg
    elif status_code == 422:
        if "email" in res_js['error']:
            assert res_js['error']['email'][0] == err_msg
        elif "password" in res_js['error']:
            assert res_js['error']['password'][0] == err_msg
