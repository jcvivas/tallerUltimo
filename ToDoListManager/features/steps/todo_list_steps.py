from behave import given, when, then
from todo_list import add_task, list_tasks, complete_task, clear_tasks, update_task, search_task

@given('the to-do list is empty')
def step_impl(context):
    clear_tasks()

@when('the user adds a task "{task}"')
def step_impl(context, task):
    add_task(task)

@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    tasks = [t["task"] for t in list_tasks()]
    assert task in tasks, f'Task "{task}" not found in the to-do list.'

@given('the to-do list contains tasks')
def step_impl(context):
    clear_tasks()
    for row in context.table:
        add_task(row['Task'])

@when('the user lists all tasks')
def step_impl(context):
    context.output = list_tasks()

@then('the output should contain')
def step_impl(context):
    output_tasks = [t["task"] for t in context.output]
    expected_tasks = [row['Task'] for row in context.table]
    assert output_tasks == expected_tasks, f"Expected {expected_tasks}, but got {output_tasks}"

@when('the user marks task "{task}" as completed')
def step_impl(context, task):
    complete_task(task)

@then('the to-do list should show task "{task}" as completed')
def step_impl(context, task):
    for t in list_tasks():
        if t["task"] == task:
            assert t["completed"], f'Task "{task}" is not marked as completed.'
            return
    raise AssertionError(f'Task "{task}" not found.')

@when('the user clears the to-do list')
def step_impl(context):
    clear_tasks()

@then('the to-do list should be empty')
def step_impl(context):
    assert not list_tasks(), "The to-do list is not empty."

@when('the user updates the task "{old_task}" to "{new_task}"')
def step_impl(context, old_task, new_task):
    update_task(old_task, new_task)

@when('the user searches for the task "{task}"')
def step_impl(context, task):
    context.search_result = search_task(task)

@then('the result should contain "{task}"')
def step_impl(context, task):
    search_result = [t["task"] for t in context.search_result]
    assert task in search_result, f'Task "{task}" not found in search result.'
