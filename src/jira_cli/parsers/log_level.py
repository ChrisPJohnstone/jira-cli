from argparse import ArgumentParser, SUPPRESS
from logging import CRITICAL, DEBUG, ERROR, INFO, WARNING
from typing import Final

from ._base import inheritable_parser

HELP_STRING: Final[str] = """
Configure the logging level.
Documentation: https://docs.python.org/3/library/logging.html#levels
"""
CHOICES: Final[list[int]] = [DEBUG, INFO, WARNING, ERROR, CRITICAL]
METAVAR: Final[str] = "LOG_LEVEL"


def log_level() -> ArgumentParser:
    """
    Creates an argument parser for log level configuration.

    Returns:
        ArgumentParser: The configured argument parser for log level.
    """
    return inheritable_parser(
        arg_names=["--log-level"],
        arg_type=int,
        choices=CHOICES,
        default=SUPPRESS,
        help=HELP_STRING.strip(),
        metavar=METAVAR,
    )
