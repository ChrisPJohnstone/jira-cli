from typing import Final

from . import config
from .parsers import shared_parsers
from constants import EnumCommands
from type_definitions import CommandModule

COMMANDS: Final[dict[EnumCommands, CommandModule]] = {
    EnumCommands.CONFIG: config,
}


__all__: list[str] = ["COMMANDS", "shared_parsers"]
