from argparse import ArgumentParser
from collections.abc import Callable
from typing import Any

from ._base import inheritable_parser


def identifier(help_str: str, arg_type: Callable[[str], Any] = int) -> ArgumentParser:
    """
    Creates an inheritable argument parser for a unique identifier.

    Returns:
        ArgumentParser: The configured argument parser for limit.
    """
    return inheritable_parser(
        arg_names=["--id"],
        arg_type=arg_type,
        required=True,
        help=help_str,
    )
