Feature: Testing Main Page Clickable Links and Website titles

  @smoke @staniscoding
  Scenario Outline: Assert Main Page Links are clickable
    Examples:
    |network  | title |
    | Instagram | ShoppingGives (@shoppinggives) • Instagram photos and videos |
    | Twitter   | hoppingGives (@ShoppingGives) / Twitter                      |
    |Facebook   | ShoppingGives - Home                                         |
    | LinkedIn  |ShoppingGives                                                 |
    Given Open Main Page
    When On main page click on <network> link
    Then Verify the network page title is <title>
