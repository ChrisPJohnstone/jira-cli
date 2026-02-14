from enum import StrEnum, unique


@unique
class BoardType(StrEnum):
    KANBAN = "kanban"
    SCRUM = "scrum"
    SIMPLE = "simple"
