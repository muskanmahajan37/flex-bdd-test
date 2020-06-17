@multiple-test
Feature: Register
  As a user I want to register in the system,
  so I can access platform-features

  Background:
    Given API endpoint for user registration

  Scenario Outline: User Registration with different inputs
    When  Required data for registration are set "<email>","<password>","<full_name>,<username>"
    And   POST request is made to endpoint with given data
    Then  Response status code should be "<status_code>"

    Examples:
      | email             | password | full_name     | status_code | username     |
      | val@gmail.com     | 1        | Valon Januzaj | 201         | vjanzzz      |
      | val@hotmail.com   | 123123   | Janz Val      | 201         | testusername |
      |                   | 123123   | Val Janz      | 422         | usertest     |
      | val@hotmail.com   | 123123   | Val Janz      | 500         | janzjanz     |
      | taulant@gmail.com | 123123   | Tal Dema      | 201         | tdemadeam    |