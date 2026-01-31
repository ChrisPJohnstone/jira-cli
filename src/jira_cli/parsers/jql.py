from argparse import ArgumentParser

from ._base import inheritable_parser


def jql(
    help_str: str,
    default: str | None = None,
    required: bool = True,
) -> ArgumentParser:
    """
    Creates an inheritable argument parser for a JQL query.

    Args:
        help_str (str): The help string for the argument.
        default (str | None): The default value for the argument. No default is set if None.
        required (bool): Whether the argument is required. Defaults to True.

    Returns:
        ArgumentParser: The configured argument parser for JQL.
    """
    if default is not None:
        help_str += f" Default: {default}"
    return inheritable_parser(
        arg_names=["--jql"],
        arg_type=str,
        required=required,
        default=default,
        help=help_str.strip(),
    )
