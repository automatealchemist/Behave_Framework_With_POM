Feature: Register New User

  @register
  Scenario: Register with mandatory fields
    Given I navigate to Register Page
    When I enter mandatory fields
    |first_name|last_name|phone_number|password  |confirm_password|
    |abc       |xyz      |1234567890  |1234567890|1234567890       |
    And I select Privacy Policy Options
    And I click on Continue button
    Then Account should get created

  @register_all_fields
  Scenario: Register with all fields
    Given I navigate to Register Page
    When I enter all fields
      |first_name|last_name|phone_number|password  |confirm_password|
      |abc       |xyz      |1234567890  |1234567890|1234567890       |
    And I select Privacy Policy Options
    And I click on Continue button
    Then Account should get created

  Scenario: Register with all fields without entering email address
    Given I navigate to Register Page
    When I enter all fields except email address
    And I select Privacy Policy Options
    And I click on Continue button
    Then Proper warning message should be visible informing about missing of email field

  Scenario: Register with duplicate email address
    Given I navigate to Register Page
    When I enter all fields except email address
    And I enter existing email address into email fields
    And I select Privacy Policy Options
    And I click on Continue button
    Then Proper warning message informing about duplicate account should be displayed.

    Scenario: Register without providing any details
      Given I navigate to Register page
      When I donot enter anything into the fields
      And I select Privacy Policy Options
      And I click on Continue button
      Then Proper writing message for every mandatory fields should be displayed