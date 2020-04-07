@awsLogin
Feature: Make login in the aws account
  As an aws User
  I want to make Login in the aws account

  @loginSuccessfull
  Scenario: Login successfull
    Given I am an aws user
    When I Login aws account
    Then Login is successfull


