from argparse import ArgumentParser

from jira_cli.parsers import identifier


def command_parsers() -> list[ArgumentParser]:
    return [identifier(help_str="The ID of the issue to view.", arg_type=str)]
