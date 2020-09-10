@ui
Feature: User login
  As a user,
  I want to login
  So I can access my account

  Scenario: Login
    Given the user is on login page
    When the user enters email "user@test.com" and password "12345"
    Then User should see homepage dashboard

  Scenario: Login with wrong credentials
    Given the user is on login page
    When the user tries to login with "notexist@test.com" and password "P@ssw0rd"
    Then User should see message "Auth failed"

  Scenario: Login with invalid email format
    Given the user is on login page
    When the user tries to login entering  email "email123" and  password "P@ssw0rd"
    Then User should see error message "Enter a valid email address"

  Scenario: Login missing parameters
    Given the user is on login page
    When the user leaves email as blank and password as blank and clicks login
    Then User should see error messages "This field is required"


