Feature: Manage ToDo List
  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task Buy groceries
    Then the to-do list should contain Buy groceries
  Scenario: List all tasks in the to-do list
    Given the todo list contains tasks:
      | Task           |
      | Buy groceries  |
      | Pay bills      |
    When the user lists all tasks
    Then the output should contain:
      | Task           |
      | Buy groceries  |
      | Pay bills      |
  Scenario: Mark a task as completed
    Given the todo list contains tasks:
      | Task          | Status  |
      | Buy groceries | Pending |
    When the user marks task Buy groceries as completed
    Then the todo list should show task Buy groceries as completed
  Scenario: Clear the entire to-do list
    Given the todo list contains tasks:
      | Task          |
      | Buy groceries |
      | Pay bills     |
    When the user clears the todo list
    Then the todo list should be empty

