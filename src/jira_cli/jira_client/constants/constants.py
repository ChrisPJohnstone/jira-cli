from typing import Final


JIRA_CLOUD_PREFIX: Final[str] = "/rest/api/3"
JIRA_SOFTWARE_CLOUD_PREFIX: Final[str] = "/rest/agile/1.0"
ENDPOINT_DASHBOARD: Final[str] = f"{JIRA_SOFTWARE_CLOUD_PREFIX}/board"
ENDPOINT_SEARCH: Final[str] = f"{JIRA_CLOUD_PREFIX}/search/jql"
