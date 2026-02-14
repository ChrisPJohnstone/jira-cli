from enum import StrEnum, unique


@unique
class EnumSubCommands(StrEnum):
    SEARCH = "list"
    SHOW = "show"
    ISSUES = "issues"
