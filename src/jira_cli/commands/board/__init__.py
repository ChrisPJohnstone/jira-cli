from . import issues, search
from .parsers import command_parsers
from jira_cli.constants import EnumSubCommands
from jira_cli.type_definitions import SubCommandsProperty


SUBCOMMANDS: SubCommandsProperty = {
    EnumSubCommands.ISSUES: issues,
    EnumSubCommands.SEARCH: search,
}

__all__: list[str] = ["SUBCOMMANDS", "command_parsers"]
