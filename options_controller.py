from json_operations import get_tasks_from_json, edit_task_into_json, remove_task_from_json

MENU = """Please select your option :
    1 - Add new task
    2 - Show tasks list
    3 - Mark task as completed
    4 - Delete task
    5 - Exit application
    """

def show_menu() -> int:
    print("-" * 40)
    print(MENU)
    available_inputs = ["1", "2", "3", "4", "5"]
    choice_input = input("Enter the option's number >> ").strip()
    print("")
    while choice_input not in available_inputs:
        print("Invalid input. Make sure to enter a number between 1 and 5.")
        print("")
        print(MENU)
        print("")
        choice_input = input("Enter the option's number >> ").strip()
    return int(choice_input)

def show_tasks_list():
    print("x" * 40)
    print("Your tasks list :")
    for task in get_tasks_from_json():
        if task['done']:
            done_str = "[X]"
        else:
            done_str = "[ ]"
        print(f"    - (N°{task['id']}) {task['title']} {done_str}")
    print("x" * 40)

def mark_task_done() -> None:
    show_tasks_list()
    task_to_edit_id = input("Enter the ID of the task you just completed >> ").strip()
    while not is_task_id_input_valid(task_to_edit_id):
        task_to_edit_id = input("Enter the ID of the task you just completed >> ").strip()
    edit_task_into_json(int(task_to_edit_id))

def delete_task() -> None:
    show_tasks_list()
    task_to_delete_id = input("Enter the ID of the task you want to delete >> ").strip()
    while not is_task_id_input_valid(task_to_delete_id):
        task_to_delete_id = input("Enter the ID of the task you want to delete >> ").strip()

    confirm = input(f"Are you sure you want to delete task N°{task_to_delete_id}? (y/n) >> ")
    if confirm == "y":
        remove_task_from_json(int(task_to_delete_id))
    else:
        print(f"Task N°{task_to_delete_id} wasn't removed.")

def is_task_id_input_valid(focused_task_id: str) -> bool:
    available_task_ids = []
    for task in get_tasks_from_json():
        available_task_ids.append(str(task['id']))

    if focused_task_id not in available_task_ids:
        print("Invalid task ID input. Please make sure to enter a valid task number...")
        return False

    try:
        int(focused_task_id)
    except TypeError:
        print("Invalid type input. You must enter a valid number from the existing task list")
        return False
    return True
