from curses import window

from ..constants import Action, Key
from ..type_definitions import Bindings
from ._jira_base import WindowJira


class WindowIssue(WindowJira):
    def _message(self, message: str) -> str:
        return f"[Issue Window] {message}"

    @property
    def BINDINGS(self) -> Bindings:
        return {
            Key.L_Q: Action.QUIT,
        }

    def action(self, action: Action) -> None:
        match action:
            case _:
                raise NotImplementedError(f"{action} is not implemented")

    def draw(self, screen: window) -> None:
        screen.clear()
        screen.addstr(0, 0, "Issue Window")
        screen.refresh()
