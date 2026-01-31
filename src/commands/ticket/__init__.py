from . import list
from .parsers import command_parsers
from constants import EnumSubCommands
from type_definitions import SubCommandsProperty


SUBCOMMANDS: SubCommandsProperty = {
    EnumSubCommands.LIST: list,
}

__all__: list[str] = ["SUBCOMMANDS", "command_parsers"]
