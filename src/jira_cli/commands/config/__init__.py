from . import show
from .parsers import command_parsers
from jira_cli.constants import SubCommands
from jira_cli.type_definitions import SubCommandsProperty


SUBCOMMANDS: SubCommandsProperty = {
    SubCommands.SHOW: show,
}

__all__: list[str] = ["SUBCOMMANDS", "command_parsers"]
