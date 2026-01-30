# CLI Todo Application

This project is part of my **Dev Journey**, a structured, project-based exploration
of the main types of software applications.

The goal of this project is to build a **simple command-line todo application**
in order to focus on core programming concepts without the complexity of a graphical interface.

---

## Project goals

- Build a functional CLI application from scratch
- Practice core programming logic
- Learn how to design a simple command-based interface
- Persist data using a lightweight format (JSON)

This project intentionally avoids advanced features to keep the scope focused and clear.

---

## Features

- Add a new task
- List existing tasks
- Mark a task as completed
- Delete a task
- Persist tasks between executions using a JSON file

---

## Technologies used

- **Python**
- **argparse** for command-line argument parsing
- **JSON** for data persistence
- Standard Python libraries only

---

## Example usage

```bash
python todo.py add "Buy groceries"
python todo.py list
python todo.py done 1
python todo.py delete 1
```

---

## Project structure

```bash
.
├── todo.py
├── data.json
└── README.md
```

---

## Key concept practiced

- Variables, conditions, and loops
- Functions and basic program structure
- Command-line interfaces (CLI)
- Argument parsing with argparse
- Reading and writing JSON files
- Error handling and input validation
- Writing clear and readable code

---

## What I learned

- How to design a simple and intuitive CLI interface
- How to separate logic from input/output
- How to persist application state between runs
- The importance of keeping a small and well-defined scope
- How small applications can still demonstrate solid engineering fundamentals

---

## Scope & limitations
- This is a local, single-user application
- No database or external services are used
- The focus is on clarity and learning, not performance or scalability

---

## How this fits into my dev journey
This project represents the starting point of my exploration of software development.
It focuses on fundamentals that are reused in nearly every other type of application,
from backend services to desktop and mobile apps.
