# Changelog

All notable changes to this project will be documented in this file.

The format is inspired by [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
and this project follows semantic versioning.

---

## [Unreleased]

### Planned
* Optional flags for commands (e.g. `--force`, filters for `list`)
* JSON output mode for scripting
* Unit tests
* Packaging as an installable CLI command

---

## [v2.0.0] – Argparse-based CLI release

### Added
* Argparse-based command-line interface
* Subcommands: `add`, `list`, `done`, `delete`
* Scriptable and automation-friendly command execution
* Robust JSON initialization and recovery
* Clear user feedback messages
* Consistent exit codes for success and failure
* Cleaner project structure with dedicated CLI and persistence layers

### Changed
* Replaced interactive menu with command-driven workflow
* Refactored user interaction logic into CLI commands
* Improved data persistence robustness and error handling
* Improved overall code readability and maintainability

### Removed
* Interactive menu system
* Runtime user input via `input()`

### Breaking changes
* The interactive menu-based interface has been removed
* All interactions must now be performed via command-line arguments

## [v1.0.0] – Initial stable version

### Added

* Interactive, menu‑based command‑line interface
* Ability to add new tasks
* Ability to list all existing tasks
* Ability to mark a task as completed
* Ability to delete a task with confirmation
* Persistent storage of tasks using a local JSON file
* Automatic initialization of the data file on first run

### Technical details

* Tasks stored as dictionaries with `id`, `title`, and `done` fields
* Incremental task ID generation
* Basic input validation for menu options and task IDs
* Clear separation between:

  * CLI / user interaction logic
  * Data persistence logic

### Notes

* This version intentionally avoids argument parsing libraries
* The application is designed for interactive use only
* Serves as a functional baseline before architectural refactoring
