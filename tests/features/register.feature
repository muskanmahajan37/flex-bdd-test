Feature: Register
  As a user I want to register in the system,
  so I can access features of the platform

  Background:
    Given API endpoint for user registration

  @correct-credentials
  Scenario: User Registration with correct credentials
    When  Required data for registration are set
    And   POST request is made to endpoint with specified data
    Then  Response status code should be 200
    And   The response body should contain id, email and hashed_password

