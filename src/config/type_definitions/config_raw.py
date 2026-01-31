from typing import TypedDict


class ConfigRaw(TypedDict):
    """TypedDict for raw configuration data."""

    base_url: str
    api_token: str
