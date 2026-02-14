from typing import Required, TypedDict

from jira_cli.type_definitions import JSONObject


class RequestKwargs(TypedDict, total=False):
    """Type definition for request kwargs."""

    url: Required[str]
    method: str
    headers: dict[str, str]
    data: JSONObject
