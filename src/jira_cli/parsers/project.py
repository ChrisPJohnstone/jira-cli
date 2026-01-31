from argparse import ArgumentParser, SUPPRESS
from typing import Final

from ._base import inheritable_parser

DEFAULT_HELP_STR: Final[str] = "The project key or ID."


def project(
    help_str: str = DEFAULT_HELP_STR,
    default: str = SUPPRESS,
) -> ArgumentParser:
    """
    Creates an inheritable argument parser for a project.

    Returns:
        ArgumentParser: The configured argument parser for limit.
    """
    if default is not SUPPRESS:
        help_str += "Default: {default}"
    return inheritable_parser(
        arg_names=["--project"],
        arg_type=str,
        default=default,
        help=help_str.strip(),
    )
