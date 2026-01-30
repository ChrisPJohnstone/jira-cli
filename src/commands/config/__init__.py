from . import show
from .parsers import command_parsers
from constants import EnumSubCommands
from type_definitions import SubCommandsProperty


SUBCOMMANDS: SubCommandsProperty = {
    EnumSubCommands.SHOW: show,
}

__all__: list[str] = ["SUBCOMMANDS", "command_parsers"]
