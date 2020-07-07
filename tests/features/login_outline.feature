@bddapi
Feature: Login
  As a user I want to login in the system,
  so I can access manage my account

  Background:
    Given  API endpoint for user login

  Scenario Outline: User Login with different inputs
    When  Required data for login are set "<email>","<password>"
    Then  POST request is made to endpoint with data provided
    And  Response message should be "<message>" and status code "<status_code>"

    Examples:
      | email         | password | status_code | message                         |
      | user@test.com | 12345    | 200         | ""                              |
      | user@test.com | 1234567  | 400         | Credentials not correct         |
      | user@test.co  | 123456   | 400         | User does not exist.            |
      |               | 123456   | 422         | The email field is required.    |
      | user@test.com |          | 422         | The password field is required. |
