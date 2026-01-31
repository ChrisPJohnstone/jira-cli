from argparse import (
    ArgumentParser,
    Namespace,
    RawTextHelpFormatter,
    _SubParsersAction,
)
from logging import Logger, basicConfig, getLogger
from pathlib import Path

from jira_cli.constants import (
    CONFIG_PATH_ARG_NAME,
    CONFIG_PATH_DEST,
    DEFAULT_CONFIG_PATH,
    DEFAULT_LOG_LEVEL,
)
from jira_cli.commands import COMMANDS, shared_parsers
from jira_cli.constants import HelpCommands, HelpSubCommands


def main_parser() -> ArgumentParser:
    """
    Create the main argument parser for the Jira CLI.

    Returns:
        ArgumentParser: The configured argument parser.
    """
    shared: list[ArgumentParser] = shared_parsers()
    parser: ArgumentParser = ArgumentParser(
        description="A Command Line Interface for Jira",
        formatter_class=RawTextHelpFormatter,
        parents=[*shared],
    )
    command_subs: _SubParsersAction = parser.add_subparsers(
        title="command",
        metavar="<command>",
        required=True,
    )
    for command, command_module in COMMANDS.items():
        command_parser: ArgumentParser = command_subs.add_parser(
            name=command,
            formatter_class=RawTextHelpFormatter,
            parents=[*shared, *command_module.command_parsers()],
            help=HelpCommands[command],
            description=HelpCommands[command],
        )
        subcommand_subs: _SubParsersAction = command_parser.add_subparsers(
            title="subcommand",
            metavar="<subcommand>",
            required=True,
        )
        for subcommand, subcommand_module in command_module.SUBCOMMANDS.items():
            subcommand_parser: ArgumentParser = subcommand_subs.add_parser(
                name=subcommand,
                formatter_class=RawTextHelpFormatter,
                parents=[*shared, *subcommand_module.command_parsers()],
                help=HelpSubCommands[command][subcommand],
                description=HelpSubCommands[command][subcommand],
            )
            subcommand_parser.set_defaults(main=subcommand_module.main)
    return parser


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
