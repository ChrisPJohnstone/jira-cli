from typing import Required, TypedDict


class ArgsSearchBoardIssues(TypedDict, total=False):
    """Type definition for search board issues arguments."""

    board_id: Required[int]
    jql: str
    limit: int
