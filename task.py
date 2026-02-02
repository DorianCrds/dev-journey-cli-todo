# task.py
import argparse
from json_operations import init_json_file

from cli_commands import (
    add_task_command,
    list_tasks_command,
    mark_task_done_command,
    delete_task_command
)

init_json_file()

def main():
    parser = argparse.ArgumentParser(
        prog="task",
        description="Command-line ToDo List application"
    )

    subparsers = parser.add_subparsers(
        title="commands",
        dest="command",
        required=True
    )

    # --- add ---
    add_parser = subparsers.add_parser(
        "add",
        help="Add a new task"
    )
    add_parser.add_argument(
        "title",
        type=str,
        help="Title of the task"
    )
    add_parser.set_defaults(func=add_task_command)

    # --- list ---
    list_parser = subparsers.add_parser(
        "list",
        help="List all tasks"
    )
    list_parser.set_defaults(func=list_tasks_command)

    # --- done ---
    done_parser = subparsers.add_parser(
        "done",
        help="Mark a task as completed"
    )
    done_parser.add_argument(
        "id",
        type=int,
        help="ID of the task to mark as done"
    )
    done_parser.set_defaults(func=mark_task_done_command)

    # --- delete ---
    delete_parser = subparsers.add_parser(
        "delete",
        help="Delete a task"
    )
    delete_parser.add_argument(
        "id",
        type=int,
        help="ID of the task to delete"
    )
    delete_parser.set_defaults(func=delete_task_command)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
