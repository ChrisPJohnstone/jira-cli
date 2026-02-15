from typing import Final

from . import board, config, issue, tui
from .parsers import shared_parsers
from jira_cli.constants import Commands
from jira_cli.type_definitions import CommandModule

COMMANDS: Final[dict[Commands, CommandModule]] = {
    Commands.BOARD: board,
    Commands.CONFIG: config,
    Commands.ISSUE: issue,
    Commands.TUI: tui,
}


__all__: list[str] = ["COMMANDS", "shared_parsers"]
