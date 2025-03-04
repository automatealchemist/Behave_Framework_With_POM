

Feature: Login with Email & Password

  @login
  Scenario Outline: Login with valid credentials
    Given I navigated to Login page
    When I enter valid email address as "<email>" and password as "<password>"
    And I click on the Login Button
    Then I should logged in
    And I click on Desktop
    Examples:
    |email                      |password |
    |abcxyz@xyz.com             | 1234567890  |



  Scenario: Login with invalid email and valid password
    Given I navigated to Login page
    When I enter invalid email address as "abcxz@xyz.com" and valid password "1234567890"
    And I click on the Login Button
    Then I should get a proper warning message

  Scenario: Login with valid email and invalid password
    Given I navigated to Login page
    When I enter valid email address as "abcxyz@xyz.com" and invalid password "14567890"
    And I click on the Login Button
    Then I should get a proper warning message

  Scenario: Login with invalid email and invalid password
    Given I navigated to Login page
    When I enter invalid email address as "abcx@xyz.com" and invalid password "14567890"
    And I click on the Login Button
    Then I should get a proper warning message

  Scenario: Login without entering any email and password
    Given I navigated to Login page
    When I donot enter anything into email address "" and password ""
    And I click on the Login Button
    Then I should get a proper warning message
