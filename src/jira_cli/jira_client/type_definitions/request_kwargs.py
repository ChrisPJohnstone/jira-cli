from typing import Required, TypedDict


class RequestKwargs(TypedDict, total=False):
    """Type definition for request kwargs."""

    url: Required[str]
    method: str
    headers: dict[str, str]
    data: bytes
