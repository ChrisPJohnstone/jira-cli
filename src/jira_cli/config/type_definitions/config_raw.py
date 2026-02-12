from typing import TypedDict


class ConfigRaw(TypedDict):
    """TypedDict for raw configuration data."""

    jira_api_token: str
    jira_base_url: str
    jira_email: str
