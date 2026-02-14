from enum import StrEnum, unique


@unique
class Commands(StrEnum):
    BOARD = "board"
    CONFIG = "config"
    ISSUE = "issue"
