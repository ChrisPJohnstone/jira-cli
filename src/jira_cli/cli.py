from argparse import ArgumentParser, Namespace
from logging import Logger, basicConfig, getLogger
from pathlib import Path

from constants import (
    CONFIG_PATH_ARG_NAME,
    CONFIG_PATH_DEST,
    DEFAULT_CONFIG_PATH,
    DEFAULT_LOG_LEVEL,
)
from jira_cli import main_parser


def main() -> None:
    """Entrypoint for the Jira CLI."""
    parser: ArgumentParser = main_parser()
    args: Namespace = parser.parse_args()
    basicConfig()
    logger: Logger = getLogger(__name__)
    logger.setLevel(level=getattr(args, "log_level", DEFAULT_LOG_LEVEL))
    logger.debug(f"Parsed arguments: {args}")
    args.logger = logger
    config_path: Path = getattr(args, CONFIG_PATH_ARG_NAME, DEFAULT_CONFIG_PATH)
    setattr(args, CONFIG_PATH_DEST, config_path)
    args.main(args)
