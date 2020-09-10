@ui
Feature: Payment
  As a user,
  I want to order
  So I can buy a service

  Scenario: Order a service
    Given user logs in their account
    Then  User navigates to programming
    Then  User clicks on a service
    Then  Chooses to pay
    Then  The payment should be finished

