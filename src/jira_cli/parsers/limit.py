from argparse import ArgumentParser

from jira_cli.constants import DEFAULT_LIMIT


def limit(default: int = DEFAULT_LIMIT) -> ArgumentParser:
    """
    Creates an inheritable argument parser for a limit integer argument.

    Returns:
        ArgumentParser: The configured argument parser for limit.
    """
    parser: ArgumentParser = ArgumentParser(add_help=False)
    parser.add_argument(
        "--limit",
        dest="limit",
        type=int,
        default=default,
        help=f"The maximum number of items. Default: {default}",
    )
    return parser
