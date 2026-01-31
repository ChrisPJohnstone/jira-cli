from argparse import ArgumentParser, SUPPRESS
from typing import Final

from ._base import inheritable_parser
from jira_cli.jira_client import BoardType

DEFAULT_HELP_STR: Final[str] = "The board type to get results for."


def board_type(
    help_str: str = DEFAULT_HELP_STR,
    default: str = SUPPRESS,
) -> ArgumentParser:
    """
    Creates an inheritable argument parser for a project.

    Returns:
        ArgumentParser: The configured argument parser for limit.
    """
    help_str += f"\nPossible values: {', '.join(list(BoardType))}. "
    if default is not SUPPRESS:
        help_str += "\nDefault: {default}"
    return inheritable_parser(
        arg_names=["--board-type"],
        arg_type=BoardType,
        choices=list(BoardType),
        default=default,
        help=help_str.strip(),
    )
