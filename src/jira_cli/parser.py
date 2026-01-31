from argparse import ArgumentParser, RawTextHelpFormatter, _SubParsersAction

from commands import COMMANDS, shared_parsers
from constants import HelpCommands, HelpSubCommands


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
