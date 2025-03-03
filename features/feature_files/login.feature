

Feature: Login with Email & Password

  @login
  Scenario: Login with valid credentials
    Given I navigated to Login page
    When I enter valid email address and password
    And I click on the Login Button
    Then I should logged in
    And I click on Desktop

  Scenario: Login with invalid email and valid password
    Given I navigated to Login page
    When I enter invalid email address and valid password
    And I click on the Login Button
    Then I should get a proper warning message

  Scenario: Login with valid email and invalid password
    Given I navigated to Login page
    When I enter valid email address and invalid password
    And I click on the Login Button
    Then I should get a proper warning message

  Scenario: Login with invalid credentials
    Given I navigated to Login page
    When I enter invalid email address and invalid password
    And I click on the Login Button
    Then I should get a proper warning message

  Scenario: Login without entering any credentials
    Given I navigated to Login page
    When I donot enter anything into email address and invalid password
    And I click on the Login Button
    Then I should get a proper warning message
