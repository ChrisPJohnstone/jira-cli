from .enum_commands import EnumCommands
from .enum_subcommands import EnumSubCommands


HelpSubCommands: dict[EnumCommands, dict[EnumSubCommands, str]] = {
    EnumCommands.BOARD: {
        EnumSubCommands.LIST: "List Jira boards.",
    },
    EnumCommands.CONFIG: {
        EnumSubCommands.SHOW: "Show Jira CLI configuration.",
    },
    EnumCommands.TICKET: {
        EnumSubCommands.LIST: "List Jira tickets",
    },
}
