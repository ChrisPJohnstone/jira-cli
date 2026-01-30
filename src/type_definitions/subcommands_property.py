from .subcommand_module import SubCommandModule
from constants import EnumSubCommands


type SubCommandsProperty = dict[EnumSubCommands, SubCommandModule]
