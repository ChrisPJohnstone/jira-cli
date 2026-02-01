# Jira CLI

## Overview

A Command Line Interface (CLI) tool for interfacing with Jira because leaving the terminal is the enemy.

Currently implemented using only [Python standard library](https://docs.python.org/3/library/index.html) because why not.

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

## Development

### Structure

- [src/jira_cli/](src/jira_cli) Source code for the CLI tool. Main package for the Jira CLI.
    - [commands/](src/jira_cli/commands/) Subpackage containing command implementations.
        - [parsers.py](src/jira_cli/commands/parsers.py) Parsers which will be inherited at all levels of command parsing.
        - `{command}/` Subpackage for each command.
            Example: [board/](src/jira_cli/commands/board/)
            - `parsers.py` Parsers specific to the command.
                Example: [board/parsers.py](src/jira_cli/commands/board/parsers.py)
            - `{subcommand}/` Subpackage for each subcommand.
                Example: [board/search/](src/jira_cli/commands/board/search/)
                - `main.py` Entry point for the subcommand.
                    Example: [board/search/main.py](src/jira_cli/commands/board/search/main.py)
                - `parsers.py` Parsers specific to the subcommand.
                    Example: [board/search/parsers.py](src/jira_cli/commands/board/search/parsers.py)
    - [config/](src/jira_cli/config/) Subpackage for configuration management.
    - [constants/](src/jira_cli/constants/) Subpackage for constant values used across the CLI.
    - [jira_client/](src/jira_cli/jira_client/) Subpackage for Jira API client interactions.
    - [parsers/](src/jira_cli/parsers/) Subpackage for global parsers used across commands.
    - [cli.py](src/jira_cli/cli.py) Main entry point for the CLI application.

### Development Run

- You can run the package without reinstalling it by running:
    ```bash
    python src/jira_cli
    ```

### Testing

- Running tests requires install [requirements-dev.txt](requirements-dev.txt):
    ```bash
    pip install -r requirements-dev.txt
    ```
- Run tests using pytest:
    ```bash
    pytest
    ```

## Links

- [API Documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#about)
- [Ruff](https://docs.astral.sh/ruff/) Python Linter & Formatter
