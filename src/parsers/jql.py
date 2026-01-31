from argparse import ArgumentParser

from .type_definitions import AddArgumentKwargs


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
    kwargs: AddArgumentKwargs = {
        "type": str,
        "required": required,
        "help": help_str.strip(),
    }
    if default is not None:
        kwargs["default"] = default
        kwargs["help"] += f" Default: {default}"
    parser: ArgumentParser = ArgumentParser(add_help=False)
    parser.add_argument("--jql", **kwargs)
    return parser
