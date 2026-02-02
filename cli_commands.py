# cli_commands.py

import sys
from json_operations import (
    save_task_into_json,
    get_tasks_from_json,
    edit_task_into_json,
    remove_task_from_json
)


def add_task_command(args) -> None:
    """
    Add a new task to the JSON storage.
    """
    save_task_into_json(args.title)
    print(f"[✔] Task added: {args.title}")
    sys.exit(0)


def list_tasks_command(args) -> None:
    """
    Display all tasks stored in the JSON file.
    """
    tasks = get_tasks_from_json()

    if not tasks:
        print("[i] No tasks found.")
        sys.exit(0)

    print("\nYour tasks list:")
    print("-" * 40)
    for task in tasks:
        status = "[X]" if task["done"] else "[ ]"
        print(f"{task['id']:>3} {status} {task['title']}")
    print("-" * 40)
    sys.exit(0)


def mark_task_done_command(args) -> None:
    """
    Mark a task as completed using its ID.
    """
    success = edit_task_into_json(args.id)
    if success:
        print(f"[✔] Task {args.id} marked as done.")
        sys.exit(0)
    else:
        print(f"[✖] Task with ID {args.id} does not exist.")
        sys.exit(1)


def delete_task_command(args) -> None:
    """
    Delete a task using its ID.
    """
    success = remove_task_from_json(args.id)
    if success:
        print(f"[✔] Task {args.id} deleted.")
        sys.exit(0)
    else:
        print(f"[✖] Task with ID {args.id} does not exist.")
        sys.exit(1)
