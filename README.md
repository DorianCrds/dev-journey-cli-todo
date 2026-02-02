# CLI Todo Application (V1)

This project is part of my **Dev Journey**, a structured, project‑based exploration of core software development concepts.

The goal of this project is to build a **simple command‑line Todo application** using Python, focusing on logic, structure, and data persistence without introducing external dependencies or advanced tooling.

This README reflects the state of the project at **version v1.0.0**.

---

## Project goals

* Build a functional CLI application from scratch
* Practice core programming logic (loops, conditions, functions)
* Design a simple, menu‑driven command‑line interface
* Persist user data between executions using a JSON file

The scope is intentionally limited to keep the focus on fundamentals.

---

## Features (V1)

* Interactive menu displayed in the terminal
* Add a new task
* Display the list of existing tasks
* Mark a task as completed
* Delete a task with confirmation
* Persistent storage using a local JSON file (`data.json`)
* Basic input validation and error handling

---

## How it works

When the application starts:

* A `data.json` file is automatically created if it does not exist
* The user is greeted with a menu‑based interface
* The application runs in a loop until the user chooses to exit

All interactions are handled through standard input/output (`input()` / `print()`), making the flow explicit and easy to follow.

---

## Technologies used (V1)

* **Python 3**
* **JSON** for data persistence
* Python standard library only (`json`, `pathlib`, `os`)

> ⚠️ Note: Argument parsing libraries such as `argparse` are **not used in V1**. The CLI is entirely menu‑driven.

---

## Example session

```text
Welcome to your command-line ToDoList Application !
----------------------------------------
Please select your option :
    1 - Add new task
    2 - Show tasks list
    3 - Mark task as completed
    4 - Delete task
    5 - Exit application

Enter the option's number >> 1
Enter the new task title >> Buy groceries
```

---

## Project structure (V1)

```bash
.
├── main.py                # Application entry point
├── options_controller.py  # Menu and user interactions
├── json_operations.py     # Data persistence logic
├── data.json              # Tasks storage (auto‑generated)
├── CHANGELOG.md
└── README.md
```

---

## Key concepts practiced

* Program flow control (while loops, conditionals)
* Function design and separation of concerns
* Input validation and user feedback
* File I/O and JSON manipulation
* Simple state persistence
* Readable and maintainable code structure

---

## Scope & limitations

* Local, single‑user application
* No command‑line arguments or subcommands
* No concurrency or multi‑user support
* No external dependencies

These limitations are intentional and serve as a foundation for future iterations.

---

## Next steps

The next major version (V2) will introduce:

* A true command‑line interface using `argparse`
* Subcommands instead of an interactive menu
* Clearer UX for scripting and automation use cases

This refactor will focus on improving extensibility and CLI ergonomics while preserving the existing core logic.

---

## How this fits into my dev journey

This project represents an early but important milestone in my learning path. It focuses on transferable fundamentals that apply to nearly all types of applications, from backend services to desktop and automation tools.
