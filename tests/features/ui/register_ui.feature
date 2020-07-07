@selenium
Feature: User Register
  As a user,
  I want to register
  So I can access my account

  Scenario: Login
    Given API endpoint for flex-homepage is given
    Given FLEX homepage is shown
    When  User clicks Sign Up
    Then  Types name,username,email,password,and confirm password
    Then  User clicks submit button
