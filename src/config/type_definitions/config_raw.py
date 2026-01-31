from typing import TypedDict


class ConfigRaw(TypedDict):
    """TypedDict for raw configuration data."""

    jira_base_url: str
    jira_api_token: str
