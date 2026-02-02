import json
import pathlib
import os
import sys

DATA_FILE_PATH = pathlib.Path(os.path.join(pathlib.Path().resolve(), "data.json"))


def init_json_file() -> None:
    """
    Ensure the JSON file exists and contains a 'tasks' list.
    If the file is missing, empty, or corrupted, it will be initialized.
    """
    if not DATA_FILE_PATH.is_file():
        _write_tasks([])
        return

    try:
        with open(DATA_FILE_PATH, "r") as f:
            data = json.load(f)
        if "tasks" not in data or not isinstance(data["tasks"], list):
            raise ValueError
    except (json.JSONDecodeError, ValueError):
        # Initializes file if missing, empty or corrupted
        _write_tasks([])


def _write_tasks(tasks: list) -> None:
    """Writes tasks list in JSON file."""
    try:
        with open(DATA_FILE_PATH, "w") as f:
            json.dump({"tasks": tasks}, f, indent=4)
    except Exception as e:
        print(f"[✖] Error writing to JSON file: {e}")
        sys.exit(1)


def get_tasks_from_json() -> list:
    """
    Always return a task list.
    Even if the file is empty or missing.
    """
    try:
        with open(DATA_FILE_PATH, "r") as f:
            data = json.load(f)
        tasks = data.get("tasks")
        if not isinstance(tasks, list):
            raise ValueError
        return tasks
    except (FileNotFoundError, json.JSONDecodeError, ValueError):
        # Initializes file and returns empty list
        _write_tasks([])
        return []


def save_task_into_json(new_task_title: str) -> None:
    """Adds and saves a new task to JSON."""
    tasks = get_tasks_from_json()
    new_id = max((task["id"] for task in tasks), default=0) + 1

    new_task = {
        "id": new_id,
        "title": new_task_title,
        "done": False
    }
    tasks.append(new_task)
    _write_tasks(tasks)


def edit_task_into_json(task_id: int) -> bool:
    """Marks task as done. Returns True if success, False if ID not found."""
    tasks = get_tasks_from_json()
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            _write_tasks(tasks)
            return True
    return False


def remove_task_from_json(task_id: int) -> bool:
    """Deletes task for ID. Returns True if success, False if ID not found."""
    tasks = get_tasks_from_json()
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            _write_tasks(tasks)
            return True
    return False
