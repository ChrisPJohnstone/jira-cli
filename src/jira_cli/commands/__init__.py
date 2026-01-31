from typing import Final

from . import board, config, ticket
from .parsers import shared_parsers
from jira_cli.constants import EnumCommands
from jira_cli.type_definitions import CommandModule

COMMANDS: Final[dict[EnumCommands, CommandModule]] = {
    EnumCommands.BOARD: board,
    EnumCommands.CONFIG: config,
    EnumCommands.TICKET: ticket,
}


__all__: list[str] = ["COMMANDS", "shared_parsers"]
