@ui
Feature: Service
  As a user,
  I want to create service,
  So I can sell my services, and get work

  Scenario: Create new service
    Given API endpoint for flex-homepage is given
    Given FLEX homepage is shown
    When  User clicks login
    Then  Types username and password
    Then  User should see homepage
    Then  User clicks profile icon
    And   Selects Profile
    And   Press Create Service button
    Then  Fill all the fields
    And   Click create new service
    Then  Service should be created

