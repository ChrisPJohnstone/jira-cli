from typing import TypedDict


class SearchBoardsArgs(TypedDict, total=False):
    """Type definition for search boards arguments."""

    board_type: str
    name: str
    project: str
    limit: int
