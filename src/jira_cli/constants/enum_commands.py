from enum import StrEnum, unique


@unique
class EnumCommands(StrEnum):
    BOARD = "board"
    CONFIG = "config"
    ISSUE = "issue"
