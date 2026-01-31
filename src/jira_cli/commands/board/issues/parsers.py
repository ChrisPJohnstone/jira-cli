from argparse import ArgumentParser

from jira_cli.parsers import id, jql, limit


def command_parsers() -> list[ArgumentParser]:
    return [
        id("The ID of the board to list issues from."),
        jql("JQL query to filter issues on the board."),
        limit(),
    ]
