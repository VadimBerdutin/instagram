Feature: Login
  Check user can login with valid username and password

#  Scenario: Valid login
#    Given I open login page
#    When I type "holy_hedgehog___" in username field
#    When I type "ESqwerty5892" in password field
#    When I click login button

  Scenario: Valid login
    Given I open login page
    When I type "holy_hedgehog___" in username field
    When I type "ESqwerty5892" in password field
    When I click element with text "Log In"
    Then I see element with text "Turn on Notifications"

#  Scenario: Valid login
#    Given I log in

#  Scenario: Invalid login
#    Given I open login page
#     When I type "werqwe" in username field
#     When I type "qwerqwe" in password field
#     When I click element with text "Log In"
#     Then I see element with text "Sorry, your password was incorrect"
#
#     When I type "1234qwe" in username field
#     When I type "1234qwe" in password field
#     When I click element with text "Log In"
#     Then I see element with text "The username you entered doesn't belong to an account"
#
#     When I type "!@$%" in username field
#     When I type "!@$%" in password field
#     When I click element with text "Log In"
#     Then I see element with text "The username you entered doesn't belong to an account"

#  Scenario Outline: Invalid Login
#    Given I open login page
#    When I type "<username>" in username field
#    When I type "<password>" in password field
#    When I click element with text "Log In"
#    Then I see element with text "<text>"
#
#    Examples:
#      | username | password | text                                                  |
#      | werqwe   | qwerqwe  | Sorry, your password was incorrect                    |
#      | 1234qwe  | 1234qwe  | The username you entered doesn't belong to an account |
#      | !@$%     | !@$%     | The username you entered doesn't belong to an account |