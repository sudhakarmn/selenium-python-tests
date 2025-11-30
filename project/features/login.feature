Feature: Login Functionality
  As a user
  I want to login to the application
  So I can access secure pages

  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I enter valid username and password
    And I click the login button
    Then I should be redirected to the secure area
    And I should see a success message
