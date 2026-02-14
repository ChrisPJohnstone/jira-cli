from .enum_commands import Commands


HelpCommands: dict[Commands, str] = {
    Commands.BOARD: "Commands for interacting with Jira boards.",
    Commands.CONFIG: "Manage Jira CLI configuration.",
    Commands.ISSUE: "Commands for interacting with Jira tickets.",
}
