from argparse import ArgumentParser

from ._base import inheritable_parser
from jira_cli.constants import DEFAULT_LIMIT


def limit(default: int = DEFAULT_LIMIT) -> ArgumentParser:
    """
    Creates an inheritable argument parser for a limit integer argument.

    Returns:
        ArgumentParser: The configured argument parser for limit.
    """
    return inheritable_parser(
        arg_names=["--limit"],
        arg_type=int,
        default=default,
        help=f"The maximum number of items. Default: {default}",
    )
