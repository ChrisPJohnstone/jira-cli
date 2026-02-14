# Contributing to Jira CLI

## Contributing

Contributions must be done through a pull request with passing tests.

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

- Running tests requires installing [requirements-dev.txt](requirements-dev.txt):
    ```bash
    pip install -r requirements-dev.txt
    ```
- Run tests using pytest:
    ```bash
    pytest
    ```
