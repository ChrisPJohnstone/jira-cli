from argparse import ArgumentParser

from jira_cli.parsers import jql, limit


def command_parsers() -> list[ArgumentParser]:
    return [
        jql(
            help_str="JQL query for tickets to get.",
            required=True,
        ),
        limit(),
    ]
