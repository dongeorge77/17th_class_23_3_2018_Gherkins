# Created by ADMIN at 24-03-2019
Feature: actitime login
  # Enter feature description here

  Scenario: login validation
    Given User present with loginpage
    When Enter username
    When Enter password
    When Click on login
    Then Validate homepage