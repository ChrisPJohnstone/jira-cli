from .enum_commands import EnumCommands


HelpCommands: dict[EnumCommands, str] = {
    EnumCommands.CONFIG: "Manage Jira CLI configuration.",
    EnumCommands.TICKET: "Commands for interactign with Jira tickets.",
}
