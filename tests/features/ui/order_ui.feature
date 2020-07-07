@seleniumm
Feature: Payment
  As a user,
  I want to order
  So I can buy a service

 Scenario: Login
    Given API endpoint for flex-homepage is given
    Given FLEX homepage is shown
    When  User clicks login
    Then  Types username and password
    Then  User should see homepage
    Then  User navigates to programming
    Then  User clicks on a service
    Then  Chooses to pay

