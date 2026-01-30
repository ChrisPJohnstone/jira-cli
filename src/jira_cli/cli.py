from argparse import (
    ArgumentParser,
    Namespace,
    RawTextHelpFormatter,
    _SubParsersAction,
)
from typing import Final

from constants import EnumCommands
from parsers import log_level
from type_definitions import ParserCallable

SHARED_PARSERS: Final[set[ParserCallable]] = {
    log_level,
}


Commands: Final[dict[EnumCommands, int]] = {
    EnumCommands.CONFIG: 1,
}
# TODO: Add command (probably a protocol this time?)


def _parser() -> ArgumentParser:
    """
    Create the main argument parser for the Jira CLI.

    Returns:
        ArgumentParser: The configured argument parser.
    """
    shared: list[ArgumentParser] = [parser() for parser in SHARED_PARSERS]
    parser: ArgumentParser = ArgumentParser(
        description="A Command Line Interface for Jira",
        formatter_class=RawTextHelpFormatter,
        parents=[*shared],
    )
    command_subparsers: _SubParsersAction = parser.add_subparsers(
        title="command",
        metavar="<command>",
        required=True,
    )
    command: EnumCommands
    callable: int
    # TODO: Update type hint for callable (and maybe name)
    for command, callable in Commands.items():
        command_parser: _SubParsersAction = command_subparsers.add_parser(
            name=command,
            formatter_class=RawTextHelpFormatter,
            parents=[*shared],
            help="test",
            # TODO: Add help and description
        )
    return parser


def main() -> None:
    """Entrypoint for the Jira CLI."""
    parser: ArgumentParser = _parser()
    args: Namespace = parser.parse_args()
    print(args)
