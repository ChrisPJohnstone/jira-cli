from argparse import ArgumentParser

from jira_cli.parsers import board_type, limit, project


def command_parsers() -> list[ArgumentParser]:
    return [
        board_type("The board type to filter by."),
        project("Project key or ID to filter boards by."),
        limit(),
    ]
