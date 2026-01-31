from argparse import ArgumentParser, Namespace
from logging import Logger, basicConfig, getLogger

from jira_cli import main_parser


def main() -> None:
    """Entrypoint for the Jira CLI."""
    parser: ArgumentParser = main_parser()
    args: Namespace = parser.parse_args()
    basicConfig()
    logger: Logger = getLogger(__name__)
    logger.setLevel(level=args.log_level)
    logger.debug(f"Parsed arguments: {args}")
    args.logger = logger
