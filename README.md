# CLI Todo Application (V2)

This project is part of my **Dev Journey**, a structured, project-based exploration of core software development concepts.

[View Dev Journey GitHub 'Hub' repository](https://github.com/DorianCrds/dev-journey-static-website)

Version **v2.0.0** marks a major evolution of the project:  
the application is now a **professional, scriptable command-line tool** built with Python and `argparse`.

The focus of this version is on **CLI best practices**, clean architecture, and robustness, while keeping the project dependency-free and easy to understand.

---

## Project goals

* Build a professional command-line application using `argparse`
* Replace interactive menus with command-driven workflows
* Design a scriptable and automation-friendly CLI
* Improve robustness and error handling
* Maintain a clean separation of concerns

This version intentionally shifts from a learning-oriented UX to a **production-style CLI design**.

---

## Features (V2)

* Argparse-based command-line interface
* Subcommands:
  * `add` — add a new task
  * `list` — list existing tasks
  * `done` — mark a task as completed
  * `delete` — delete a task
* Persistent storage using a local JSON file (`data.json`)
* Automatic initialization and recovery of the JSON storage
* Clear user feedback and consistent exit codes
* Scriptable and automation-friendly behavior

---

## Usage

```bash
python task.py add "Buy groceries"
python task.py list
python task.py done 2
python task.py delete 3
```

Help is available for the main command and all subcommands :
```bash
python task.py -h
python task.py add -h
```

---

## How it works
- The JSON data file is automatically created or repaired at startup if needed
- Each command is executed directly from the command line
- No interactive prompts (input()) are used
- Each command returns a clear message and an appropriate exit code

This design makes the application suitable for : Shell scripting, Automation, CI / batch usage, PowerShell or Bash pipelines

---

## Project structure (V2)

```bash
.
├── task.py                # CLI entry point (argparse)
├── cli_commands.py        # CLI command implementations
├── json_operations.py     # Data persistence layer
├── data.json              # Tasks storage (auto-generated)
├── CHANGELOG.md
└── README.md
```

---

## Technologies used
- Python 3.11
- argparse (Python standard library)
- JSON for data persistence
- Python standard library only

No external dependencies are required.

---

## Key concepts practiced

- Argparse and subcommand-based CLI design
- Separation of concerns (CLI / business logic / persistence)
- Robust file handling and data validation
- Exit codes and CLI feedback conventions
- Scriptable and automation-friendly application design
- Semantic versioning and release management

---

## Scope & limitations

- Local, single-user application
- JSON-based storage (no database)
- No concurrency or multi-user support
- No external dependencies

These constraints are intentional and aligned with the project’s educational goals.

---

## Versioning

This project follows Semantic Versioning.
- v1.x — Interactive, menu-based CLI
- v2.x — Argparse-based, professional CLI

Version v2.0.0 introduces breaking changes compared to V1.

---

## How this fits into my dev journey

This version represents a key milestone:
the transition from a beginner-friendly interactive program to a professional command-line tool architecture.

It demonstrates the ability to:
- Refactor an existing codebase
- Improve UX without rewriting core logic
- Apply real-world CLI standards and practices
