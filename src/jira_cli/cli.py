from argparse import (
    ArgumentParser,
    Namespace,
    RawTextHelpFormatter,
    _SubParsersAction,
)
from logging import Logger, basicConfig, getLogger

from commands import COMMANDS, shared_parsers
from constants import HelpCommands, HelpSubCommands


def _parser() -> ArgumentParser:
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
            subcommand_subs.add_parser(
                name=subcommand,
                formatter_class=RawTextHelpFormatter,
                parents=[*shared, *subcommand_module.command_parsers()],
                help=HelpSubCommands[command][subcommand],
                description=HelpSubCommands[command][subcommand],
            )
    return parser


def main() -> None:
    """Entrypoint for the Jira CLI."""
    parser: ArgumentParser = _parser()
    args: Namespace = parser.parse_args()
    basicConfig()
    logger: Logger = getLogger(__name__)
    logger.setLevel(level=args.log_level)
    logger.debug(f"Parsed arguments: {args}")
    args.logger = logger
