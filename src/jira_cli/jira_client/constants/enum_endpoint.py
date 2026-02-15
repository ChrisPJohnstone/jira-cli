from enum import StrEnum, unique


@unique
class Endpoint(StrEnum):
    SEARCH_BOARD = "/board"
    SEARCH_BOARD_ISSUES = "/board/{board_id}/issue"
    SEARCH_JQL = "/search/jql"
    JQL_PARSE = "/jql/parse"
    ISSUE_GET = "/issue/{issue_id}"
