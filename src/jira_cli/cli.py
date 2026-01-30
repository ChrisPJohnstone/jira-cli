from argparse import ArgumentParser, Namespace, RawTextHelpFormatter
from typing import Final

from parsers import log_level
from type_definitions import ParserCallable

SHARED_PARSERS: Final[set[ParserCallable]] = {
    log_level,
}


def _parser() -> ArgumentParser:
    """
    Create the main argument parser for the Jira CLI.

    Returns:
        ArgumentParser: The configured argument parser.
    """
    parser: ArgumentParser = ArgumentParser(
        description="A Command Line Interface for Jira",
        formatter_class=RawTextHelpFormatter,
        parents=[parser() for parser in SHARED_PARSERS],
    )
    return parser


def main() -> None:
    """Entrypoint for the Jira CLI."""
    parser: ArgumentParser = _parser()
    args: Namespace = parser.parse_args()
    print(args)
