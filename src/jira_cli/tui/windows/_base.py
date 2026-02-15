from abc import ABC, abstractmethod
from curses import window

from ..config import ConfigWindow
from ..constants import Action
from ..type_definitions import Bindings


class Window(ABC):
    def __init__(self, window_config: ConfigWindow) -> None:
        self.window_config = window_config

    @property
    def window_config(self) -> ConfigWindow:
        """Configuration for window dimensions."""
        return self._window_config

    @window_config.setter
    def window_config(self, value: ConfigWindow) -> None:
        self._window_config = value

    @property
    def _logger(self):
        return self.window_config._logger

    @property
    def x_strt(self) -> int:
        """Starting column index for the TUI display."""
        return self.window_config.x_strt

    @property
    def y_strt(self) -> int:
        """Starting row index for the TUI display."""
        return self.window_config.y_strt

    @property
    def x_stop(self) -> int:
        """Ending column index for the TUI display."""
        return self.x_stop

    @property
    def y_stop(self) -> int:
        """Ending row index for the TUI display."""
        return self.y_stop

    @property
    def x_len(self) -> int:
        """Actual number of columns to display."""
        return self.x_len

    @property
    def y_len(self) -> int:
        """Actual number of rows to display."""
        return self.y_len

    @abstractmethod
    def _message(self, message: str) -> str:
        """
        Formats a log message with a standard prefix.

        Args:
            message (str): Message to log.

        Returns:
            str: Formatted log message.
        """

    def _log(self, level: int, message: str) -> None:
        """
        Logs a message at the specified log level.

        Args:
            level (int): Log level.
            message (str): Message to log.
        """
        self._logger.log(level, self._message(message))

    def refresh_bounds(self) -> None:
        """Refreshes the window bounds based on terminal dimensions."""
        self._logger.debug("Refreshing window bounds")
        self.window_config.refresh_bounds()

    @property
    @abstractmethod
    def BINDINGS(self) -> Bindings:
        """Mapping of key inputs to actions for this window."""

    @abstractmethod
    def action(self, action: Action) -> None:
        """
        Handles an action performed on the window.

        Args:
            action (Action): The action to handle.
        """

    @abstractmethod
    def draw(self, screen: window) -> None:
        """Draws the window content."""
