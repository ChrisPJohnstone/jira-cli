from argparse import Namespace

from jira_cli.config import Config
from jira_cli.utils import write_output


def main(args: Namespace) -> None:
    """
    Gets the current configuration and prints it to stdout.

    Args:
        args (Namespace): Parsed command-line arguments.
    """
    config: Config = Config.from_path(
        path=args.config_path,
        logger=args.logger,
    )
    write_output(config.to_dict())
