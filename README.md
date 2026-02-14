# Jira CLI

## Overview

A Command Line Interface (CLI) tool for interfacing with Jira because leaving the terminal is the enemy.

Currently implemented using only [Python standard library](https://docs.python.org/3/library/index.html) because why not.

## Roadmap

One of the main motivations for making this project (beyond personal entertainment) was because existing CLI/TUI tools didn't have great support from working for a Jira board (this does seem to be at least partially a fault of the API since it doesn't appear possible get things like swimlanes) so the project will likely be focused on that aspect of Jira.
- Board Interaction
    - [x] Get list of boards
    - [x] Get list of issues from a board
    - [ ] Get swinlames from a board
    - [ ] Get list of issues from a swimlane
- Ticket Interaction
    - [x] Get details of a ticket
    - [ ] Transition a ticket
    - [ ] Assign a ticket
    - [ ] Comment on a ticket
- Terminal User Interface (TUI)
    - [ ] Interactive ticket view
    - [ ] Interactive view for issues
        - [ ] Issues from board
        - [ ] Issues from swimlane

## Usage

### Prerequisites

- Python 3.14 or higher. Confirm version in [pyproject.toml](pyproject.toml).

### Installation

1. Clone the repository:
    ```bash
    git clone
    cd jira_cli
    ```
2. (Optional) Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. Install Package:
    ```bash
    pip install .
    ```

### Usage

- After installation, you can use the CLI tool with the following command:
    ```bash
    jira [command] [subcommand] [options]
    ```
- For example, to get a list of boards:
    ```bash
    jira board list
    ```
- To see all available commands and options, use:
    ```bash
    jira --help
    ```
- To see help for a specific command or subcommand, use:
    ```bash
    jira [command] --help
    jira [command] [subcommand] --help
    ```

## Links

- [API Documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#about)
- [ruff](https://docs.astral.sh/ruff/) Python Linter & Formatter
- [ty](https://docs.astral.sh/ty/) Python Type Checker & Language Server
