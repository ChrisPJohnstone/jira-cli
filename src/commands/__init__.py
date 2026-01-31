from typing import Final

from . import config, ticket
from .parsers import shared_parsers
from constants import EnumCommands
from type_definitions import CommandModule

COMMANDS: Final[dict[EnumCommands, CommandModule]] = {
    EnumCommands.CONFIG: config,
    EnumCommands.TICKET: ticket,
}


__all__: list[str] = ["COMMANDS", "shared_parsers"]
