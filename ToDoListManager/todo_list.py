to_do_list = []

def add_task(task):
    """Adds a task to the to-do list."""
    to_do_list.append({"task": task, "completed": False})

def list_tasks():
    """Returns all tasks in the to-do list."""
    return to_do_list

def complete_task(task):
    """Marks a task as completed."""
    for t in to_do_list:
        if t["task"] == task:
            t["completed"] = True
            return
    raise ValueError(f"Task '{task}' not found.")

def clear_tasks():
    """Clears all tasks from the to-do list."""
    to_do_list.clear()

def update_task(old_task, new_task):
    """Updates an existing task."""
    for t in to_do_list:
        if t["task"] == old_task:
            t["task"] = new_task
            return
    raise ValueError(f"Task '{old_task}' not found.")

def search_task(task):
    """Searches for a task in the to-do list."""
    return [t for t in to_do_list if t["task"] == task]
