from .enum_commands import Commands
from .enum_subcommands import SubCommands


HelpSubCommands: dict[Commands, dict[SubCommands, str]] = {
    Commands.BOARD: {
        SubCommands.SEARCH: "List Jira boards.",
        SubCommands.ISSUES: "List issues for a Jira board.",
    },
    Commands.CONFIG: {
        SubCommands.SHOW: "Show Jira CLI configuration.",
    },
    Commands.ISSUE: {
        SubCommands.SEARCH: "List Jira tickets",
    },
}
