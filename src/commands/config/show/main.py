from argparse import Namespace

from config import Config


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
    print(config)
