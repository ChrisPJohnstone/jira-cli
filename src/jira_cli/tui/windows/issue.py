from curses import window
from logging import DEBUG
import json

from ..config import ConfigWindow
from ..constants import Action, Key
from ..type_definitions import Bindings
from ._jira_base import WindowJira
from jira_cli.jira_client import JiraClient
from jira_cli.type_definitions import JSONObject


class WindowIssue(WindowJira):
    def __init__(
        self,
        window_config: ConfigWindow,
        jira_client: JiraClient,
        issue_id: str,
    ) -> None:
        super().__init__(window_config, jira_client)
        self.issue_id = issue_id

    @property
    def BINDINGS(self) -> Bindings:
        return {
            Key.L_Q: Action.QUIT,
        }

    @property
    def issue_id(self) -> str:
        return self._issue_id

    @issue_id.setter
    def issue_id(self, value: str) -> None:
        self._log(DEBUG, f"Setting issue_id to {value}")
        self._issue_id: str = value
        self.reload_issue()

    @property
    def issue(self) -> JSONObject:
        # TODO: Create a dataclass for Issue instead of using JSONObject
        return self._issue

    @issue.setter
    def issue(self, value: JSONObject) -> None:
        self._log(DEBUG, f"Setting issue to {value}")
        self._issue: JSONObject = value

    def _message(self, message: str) -> str:
        return f"[Issue Window] {message}"

    def reload_issue(self) -> None:
        self._log(DEBUG, f"Reloading issue {self.issue_id}")
        self.issue = self.jira_client.get_issue(self.issue_id, ["summary"])

    def action(self, action: Action) -> None:
        match action:
            case _:
                raise NotImplementedError(f"{action} is not implemented")

    def draw(self, screen: window) -> None:
        # TODO: Make output nicer & interactive
        screen.clear()
        screen.addstr(json.dumps(self.issue, indent=2))
        screen.refresh()
