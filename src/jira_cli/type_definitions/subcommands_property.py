from .subcommand_module import SubCommandModule
from jira_cli.constants import EnumSubCommands


type SubCommandsProperty = dict[EnumSubCommands, SubCommandModule]
