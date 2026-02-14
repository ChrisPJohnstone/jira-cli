from enum import StrEnum, unique


@unique
class APIVersion(StrEnum):
    CLOUD = "/rest/api/3"
    SOFTWARE_CLOUD = "/rest/agile/1.0"
