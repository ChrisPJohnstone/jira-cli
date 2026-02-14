from .subcommand_module import SubCommandModule
from jira_cli.constants import SubCommands


type SubCommandsProperty = dict[SubCommands, SubCommandModule]
