import json
import pathlib
import os

DATA_FILE_PATH = pathlib.Path(os.path.join(pathlib.Path().resolve(), "data.json"))

def init_json_file():
    if not DATA_FILE_PATH.is_file():
        with open(DATA_FILE_PATH, 'w') as json_file:
            json.dump({"tasks": []}, json_file)

def get_tasks_from_json() -> list | None:
    try:
        with open(DATA_FILE_PATH) as json_file_to_read:
            datas = json.load(json_file_to_read)
            return datas["tasks"]
    except json.JSONDecodeError as e:
        print("Invalid JSON syntax: ", e)
    except KeyError as e:
        print("Missing key in JSON data: ", e)

def save_task_into_json(new_task_title: str) -> None:
    datas = get_tasks_from_json()
    if datas:
        new_id = max(task["id"] for task in datas) + 1
    else:
        new_id = 1

    new_task = {
        "id": new_id,
        "title": new_task_title,
        "done": False
    }
    datas.append(new_task)

    try:
        with open(DATA_FILE_PATH, 'w') as json_file_to_write:
            json.dump({"tasks": datas}, json_file_to_write)
    except Exception as e:
        print("An error occured while writing to the JSON file: ", e)

def edit_task_into_json(task_id: int):
    datas = get_tasks_from_json()
    for task in datas:
        if task['id'] == task_id:
            task['done'] = True
            break

    try:
        with open(DATA_FILE_PATH, 'w') as json_file_to_write:
            json.dump({"tasks": datas}, json_file_to_write)
    except Exception as e:
        print("An error occured while writing to the JSON file: ", e)

def remove_task_from_json(task_id: int) -> None:
    datas = get_tasks_from_json()
    for task in datas:
        if task['id'] == task_id:
            datas.remove(task)
            break

    try:
        with open(DATA_FILE_PATH, 'w') as json_file_to_write:
            json.dump({"tasks": datas}, json_file_to_write)
    except Exception as e:
        print("An error occured while writing to the JSON file: ", e)