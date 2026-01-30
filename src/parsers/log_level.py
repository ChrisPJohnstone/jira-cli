from argparse import ArgumentParser
from logging import CRITICAL, DEBUG, ERROR, INFO, WARNING
from typing import Final

BASE_HELP_STRING: Final[str] = """
Configure the logging level. Default: {default}
Documentation: https://docs.python.org/3/library/logging.html#levels
"""
CHOICES: Final[list[int]] = [DEBUG, INFO, WARNING, ERROR, CRITICAL]
METAVAR: Final[str] = "LOG_LEVEL"


def log_level(default: int = WARNING) -> ArgumentParser:
    """
    Creates an argument parser for log level configuration.

    Returns:
        ArgumentParser: The configured argument parser for log level.
    """
    parser: ArgumentParser = ArgumentParser(add_help=False)
    parser.add_argument(
        "--log-level",
        type=int,
        metavar=METAVAR,
        choices=CHOICES,
        default=default,
        help=BASE_HELP_STRING.format(default=default).strip(),
    )
    return parser
