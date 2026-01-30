from argparse import ArgumentParser
from logging import CRITICAL, DEBUG, ERROR, INFO, NOTSET, WARNING
from typing import Final

BASE_HELP_STRING: Final[str] = """
Configure the logging level. Default: {default}

https://docs.python.org/3/library/logging.html#levels
"""


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
        choices=[NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL],
        default=default,
        help=BASE_HELP_STRING.format(default=default).strip(),
    )
    return parser
