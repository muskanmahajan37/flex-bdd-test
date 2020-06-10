import requests
from faker import Faker
from pytest_bdd import scenario, given, when, then, parsers

from .conftest import BDD_BASE_URL

fake = Faker()


@scenario("../features/category.feature", "Add new Category")
def test_categories():
    pass


@scenario("../features/category.feature", "Get category by id")
def test_categories_by_id():
    pass


@scenario("../features/category.feature", "Get all categories")
def test_get_all_categories():
    pass


NUMBER_EXTRA = {
    "Number": int
}


@when("POST request is made to endpoint with data and access token")
def post_request(categories_endpoint, user_logged_in):
    categories_data = {
        "name": fake.name(),
        "description": fake.name()
    }

    global req_categories
    req_categories = requests.post(
        f"{BDD_BASE_URL}/categories", json=categories_data, headers=user_logged_in
    )
    res_json = req_categories.json()
    print(res_json)


@then("Response status should be 200")
def status_code():
    assert req_categories.status_code == 200


# Scenario 2

@given("API endpoint to retrieve category by id")
def category_by_id():
    CATEGORY_BY_ID = f"{BDD_BASE_URL}/categories"
    return CATEGORY_BY_ID


@when('Get request is made to the endpoint with the id of the category')
def get_category_by_id(category_by_id, user_logged_in):
    global request_category
    request_category = requests.get(
        f"{category_by_id}/1", headers=user_logged_in
    )


@then(parsers.cfparse('Response status should be "{status_code:Number}" and the category should be retrieved',
                      extra_types=NUMBER_EXTRA))
def category_status(status_code):
    assert request_category.status_code == status_code


@then('Response should contain category name,description,subcategories')
def response_data():
    response_json = request_category.json()
    assert "description" in response_json
    assert "name" in response_json
    assert "subcategories" in response_json


# scenario 3

@when("Get request is made to categories endpoint")
def get_all_categories(categories_endpoint):
    global categories_all
    categories_all = requests.get(
        categories_endpoint
    )


@then("Response status should should be 200 and all categories should be returned")
def categories_all_status():
    assert categories_all.status_code == 200


@then("More than 5 categories should be returned")
def result_excepted():
    assert len(categories_all.json()) > 5
    assert "id" in categories_all.json()[0]
    assert "name" in categories_all.json()[0]
