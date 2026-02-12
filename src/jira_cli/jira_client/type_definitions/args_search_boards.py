from typing import TypedDict

from jira_cli.jira_client import BoardType


class ArgsSearchBoards(TypedDict, total=False):
    """Type definition for search boards arguments."""

    board_type: BoardType
    name: str
    project: str
    limit: int
