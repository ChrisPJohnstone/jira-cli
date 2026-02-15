from logging import DEBUG

from ._base import Window
from ..config import ConfigWindow
from jira_cli.jira_client import JiraClient


class WindowJira(Window):
    def __init__(
        self,
        window_config: ConfigWindow,
        jira_client: JiraClient,
    ) -> None:
        super().__init__(window_config)
        self.jira_client = jira_client

    @property
    def jira_client(self) -> JiraClient:
        """JiraClient instance for accessing Jira API."""
        return self._jira_client

    @jira_client.setter
    def jira_client(self, value: JiraClient) -> None:
        self._log(DEBUG, "Setting Jira Client")
        self._jira_client: JiraClient = value
