from enum import StrEnum, unique


@unique
class JQLValidation(StrEnum):
    NONE = "none"
    WARN = "warning"
    STRICT = "strict"
