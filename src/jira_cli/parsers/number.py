from argparse import ArgumentParser, SUPPRESS
from pathlib import Path
from typing import Final

from .type_definitions import AddArgumentKwargs

DEFAULT_ARG_NAME: Final[str] = "path"


def integer(
    help_str: str,
    arg_name: str = DEFAULT_ARG_NAME,
    dest: str | None = None,
    default: str | Path = SUPPRESS,
) -> ArgumentParser:
    """
    Creates an inheritable argument parser for a filesystem path.

    Args:
        help_str (str): The help string for the argument.
        arg_name (str): The name of the argument. Defaults to "path".
        dest (str): The destination attribute name for the parsed argument. Defaults to arg_name with hyphens replaced by underscores.
        default (str | Path): The default value for the argument. Defaults to SUPPRESS.

    Returns:
        ArgumentParser: The configured argument parser for log level.
    """
    kwargs: AddArgumentKwargs = {
        "dest": dest or arg_name.replace("-", "_"),
        "type": Path,
        "default": default,
        "help": help_str.strip(),
    }
    if default is not SUPPRESS:
        kwargs["help"] += f" Default: {default}"
    parser: ArgumentParser = ArgumentParser(add_help=False)
    parser.add_argument(f"--{arg_name}", **kwargs)
    return parser
