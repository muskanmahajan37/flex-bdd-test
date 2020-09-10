@ui
Feature: User Register
  As a user,
  I want to register
  So I can access my account

  Scenario: Signup
    Given the user is on register page
    When  the user enters name "Filan" ,username "filani01" ,email "filan@gmail.com",password "123123" ,and confirm password "123123"
    Then  User account should be created, and user should be redirected to home page

  Scenario: Signup with empty fields
    Given the user is on register page
    When  the user leaves all the fields blank
    Then  All the fields should show error message "This field is required"

  Scenario: Signup with bad username
    Given the user is on register page
    When  the user enters short username "AB"
    Then  the user should see error "Enter a valid username

