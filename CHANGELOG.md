# Changelog

All notable changes to this project will be documented in this file.

The format is inspired by [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
and this project follows semantic versioning.

---

## [Unreleased]

### Planned

* Migrate from a menu‑based CLI to a command‑driven interface using `argparse`
* Introduce subcommands (add, list, done, delete)
* Improve error handling and help messages
* Make the application easier to script and automate

---

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
