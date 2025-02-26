Feature: Search any product

  @first
  Scenario: Search for a valid product
    Given I got navigated to Homepage
    When I enter valid product name in search box field
    And I click on the search button
    Then Valid product should be visible in the search result

  @first
  Scenario: Search for a invalid product
    Given I got navigated to Homepage
    When I enter invalid product name in search box field
    And I click on the search button
    Then proper message should be visible in the search result

  @first
  Scenario: Search without entering any product
    Given I got navigated to Homepage
    When I donot enter anything in the search box field
    And I click on the search button
    Then proper message should be visible in the search result
