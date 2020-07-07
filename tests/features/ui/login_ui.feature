@selenium
Feature: User login
  As a user,
  I want to login
  So I can access my account

  Scenario: Login
    Given API endpoint for flex-homepage is given
    Given FLEX homepage is shown
    When  User clicks login
    Then  Types username and password
    Then  User should see homepage

