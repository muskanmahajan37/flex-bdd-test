# Created by MROBOT at 6/10/2020
Feature: #Enter feature name here
  # Enter feature description here

  Scenario: Create new service
    Given API endpoint for services
    Given User is logged in
    When  Data to create service a new service are set
    When  User makes a post request to services endpoint with authentication headers
    Then  The response status code should be 200
    Then  Message should be Successfully created Service!
    And   Response should contain Service key
