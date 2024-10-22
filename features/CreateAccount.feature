
Feature: User Create Account functionality and Login

  @Create
  Scenario: Create User Account
    Given I got Home page
    Then User click on the Account button
    And User click on the Register button
    Then User Enter Your Personal Details
    And User Enter strong Password
    And User click on the Newsletter 'Yes' button
    Then User click on the agree button
    Then User click on the continue
    And User verify the account create successful
    Then User Logout the create account
    Then User click continue


  @Login
  Scenario: Login user functionality
    Given I got Home page
    Then User click on the Account button
    And User click on the Login button
    Then User Enter the Email and Password
    And User Verify the Login successful

