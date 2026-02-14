from argparse import ArgumentParser

from ._base import inheritable_parser


def identifier(help_str: str) -> ArgumentParser:
    """
    Creates an inheritable argument parser for a limit integer argument.

    Returns:
        ArgumentParser: The configured argument parser for limit.
    """
    return inheritable_parser(
        arg_names=["--id"],
        arg_type=int,
        required=True,
        help=help_str,
    )
