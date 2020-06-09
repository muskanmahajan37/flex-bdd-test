Feature: Categories
  As a user I want to add categories

  Background:
    Given API endpoint for categories

  Scenario: Add new Category
    Given User is logged in
    When  POST request is made to endpoint with data and access token
    Then  Response status should be 200


