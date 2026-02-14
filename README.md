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

## Links

- [API Documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#about)
- [ruff](https://docs.astral.sh/ruff/) Python Linter & Formatter
- [ty](https://docs.astral.sh/ty/) Python Type Checker & Language Server
