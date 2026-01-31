from typing import Final


JIRA_CLOUD_PREFIX: Final[str] = "/rest/api/3"
JIRA_SOFTWARE_CLOUD_PREFIX: Final[str] = "/rest/agile/1.0"
ENDPOINT_SEARCH_BOARD: Final[str] = f"{JIRA_SOFTWARE_CLOUD_PREFIX}/board"
ENDPOINT_SEARCH_BOARD_ISSUES: Final[str] = f"{ENDPOINT_SEARCH_BOARD}/{{board_id}}/issue"
ENDPOINT_SEARCH_JQL: Final[str] = f"{JIRA_CLOUD_PREFIX}/search/jql"
