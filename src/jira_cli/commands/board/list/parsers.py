from argparse import ArgumentParser

from jira_cli.parsers import limit


def command_parsers() -> list[ArgumentParser]:
    return [
        limit(),
    ]
