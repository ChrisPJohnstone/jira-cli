from .enum_commands import EnumCommands


HelpCommands: dict[EnumCommands, str] = {
    EnumCommands.BOARD: "Commands for interacting with Jira boards.",
    EnumCommands.CONFIG: "Manage Jira CLI configuration.",
    EnumCommands.TICKET: "Commands for interacting with Jira tickets.",
}
