from argparse import ArgumentParser

from jira_cli.parsers import identifier, jql, limit


def command_parsers() -> list[ArgumentParser]:
    return [
        identifier("The ID of the board to list issues from."),
        jql("JQL query to filter issues on the board."),
        limit(),
    ]
