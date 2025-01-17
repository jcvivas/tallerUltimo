Feature: Manage To-Do List

  @debug
  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"

  @debug
  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks
      | Task          |
      | Buy groceries |
      | Pay bills     |
    When the user lists all tasks
    Then the output should contain
      | Task          |
      | Buy groceries |
      | Pay bills     |

  @debug
  Scenario: Mark a task as completed
    Given the to-do list contains tasks
      | Task          | Status  |
      | Buy groceries | Pending |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

  @debug
  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks
      | Task          |
      | Buy groceries |
      | Pay bills     |
    When the user clears the to-do list
    Then the to-do list should be empty

  @debug
  Scenario: Update a task in the to-do list
    Given the to-do list contains tasks
      | Task          |
      | Buy groceries |
    When the user updates the task "Buy groceries" to "Buy groceries and milk"
    Then the to-do list should contain "Buy groceries and milk"

  @debug
  Scenario: Search for a task in the to-do list
    Given the to-do list contains tasks
      | Task          |
      | Buy groceries |
      | Pay bills     |
    When the user searches for the task "Pay bills"
    Then the result should contain "Pay bills"
