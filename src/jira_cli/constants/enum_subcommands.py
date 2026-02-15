from enum import StrEnum, unique


@unique
class SubCommands(StrEnum):
    SEARCH = "list"
    SHOW = "show"
    ISSUE = "issue"
    ISSUES = "issues"
