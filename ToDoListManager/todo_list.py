to_do_list = []
def add_task(task):
    to_do_list.append({"task": task, "completed": False})
def list_tasks():
    return to_do_list
def complete_task(task):
    for t in to_do_list:
        if t["task"] == task:
            t["completed"] = True
            return
    raise ValueError(f"Task '{task}' not found.")
def clear_tasks():
    to_do_list.clear()
if __name__ == "__main__":
    add_task("Buy groceries")
    add_task("Pay bills")
    complete_task("Buy groceries")
    print(list_tasks())
    clear_tasks()
    print(list_tasks())