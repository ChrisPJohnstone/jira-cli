from argparse import ArgumentParser

from jira_cli.parsers import limit, project


def command_parsers() -> list[ArgumentParser]:
    return [
        limit(),
        project("Project key or ID to filter boards by."),
    ]
