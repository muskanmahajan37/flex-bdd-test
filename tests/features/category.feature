@bddapi
Feature: Categories
  As a admin user want to add categories

  Scenario: Add new Category
    Given API endpoint for categories
    Given User is logged in
    When  POST request is made to endpoint with data and access token
    Then  Response status should be 200

  Scenario: Get category by id
    Given API endpoint to retrieve category by id
    Given User is logged in
    When  Get request is made to the endpoint with the id of the category
    Then  Response status should be "200" and the category should be retrieved
    Then  Response should contain category name,description,subcategories

  Scenario: Get all categories
    Given API endpoint for categories
    When  Get request is made to categories endpoint
    Then  Response status should should be 200 and all categories should be returned
    Then  More than 5 categories should be returned