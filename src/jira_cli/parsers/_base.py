from argparse import ArgumentParser
from collections.abc import Callable
from typing import Any

from .type_definitions import AddArgumentKwargs


def inheritable_parser(
    arg_names: list[str],
    arg_type: Callable[[str], Any],
    help: str,
    nargs: str | int | None = None,
    default: Any | None = None,
    choices: list[Any] | None = None,
    required: bool = False,
    metavar: str | None = None,
    dest: str | None = None,
    deprecated: bool = False,
) -> ArgumentParser:
    """
    Creates an inheritable argument parser with customizable parameters.

    Args:
        arg_names (list[str]): The names of the argument (e.g., ["--limit", "-l"]).
        help (str): The help string for the argument.
        nargs (str | int | None): The number of command-line arguments that should be consumed.
        default (Any | None): The default value for the argument. No default is set if None.
        arg_type (Callable[[str], int]): The type of the argument. Defaults to int.
        choices (list[Any] | None): A list of valid choices for the argument.
        required (bool): Whether the argument is required. Defaults to False.
        metavar (str | None): The name for the argument in usage messages.
        dest (str | None): The name of the attribute to be added to the object returned by parse_args().
        deprecated (bool): Whether the argument is deprecated. Defaults to False.

    Returns:
        ArgumentParser: The configured argument parser.
    """
    kwargs: AddArgumentKwargs = {
        "type": arg_type,
        "help": help,
    }
    if nargs is not None:
        kwargs["nargs"] = nargs
    if default is not None:
        kwargs["default"] = default
    if choices is not None:
        kwargs["choices"] = choices
    if required:
        kwargs["required"] = required
    if metavar is not None:
        kwargs["metavar"] = metavar
    if dest is not None:
        kwargs["dest"] = dest
    if deprecated:
        kwargs["deprecated"] = deprecated
    parser: ArgumentParser = ArgumentParser(add_help=False)
    parser.add_argument(*arg_names, **kwargs)
    return parser
