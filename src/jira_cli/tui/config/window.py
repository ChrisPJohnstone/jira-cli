from logging import DEBUG, Logger

from .terminal import ConfigTerminal


class ConfigWindow:
    """Configuration class for window dimensions"""

    def __init__(
        self,
        terminal_config: ConfigTerminal,
        x_strt: int = 0,
        y_strt: int = 0,
        x_len_max: int = 0,
        y_len_max: int = 0,
    ) -> None:
        """
        Initializes the config instance.

        Args:
            x_strt (int): Starting column index for the TUI display.
            y_strt (int): Starting row index for the TUI display.
            x_len_max (int): Maximum number of columns to display in the TUI.
            y_len_max (int): Maximum number of rows to display in the TUI.
        """
        self.terminal_config = terminal_config
        self.x_strt = x_strt
        self.x_len_max = x_len_max
        self.y_strt = y_strt
        self.y_len_max = y_len_max

    @property
    def terminal_config(self) -> ConfigTerminal:
        """TerminalConfig instance for accessing terminal dimensions."""
        return self._terminal_config

    @terminal_config.setter
    def terminal_config(self, value: ConfigTerminal) -> None:
        self._terminal_config: ConfigTerminal = value

    @property
    def _logger(self) -> Logger:
        return self.terminal_config._logger

    @property
    def x_max(self) -> int:
        """Maximum number of columns in the terminal."""
        return self.terminal_config.x_max

    @property
    def y_max(self) -> int:
        """Maximum number of rows in the terminal."""
        return self.terminal_config.y_max

    @property
    def x_strt(self) -> int:
        """Starting column index for the TUI display."""
        return self._x_strt

    @x_strt.setter
    def x_strt(self, value: int) -> None:
        self._log(DEBUG, f"Setting x_strt to {value}")
        self._x_strt: int = value

    @property
    def x_len_max(self) -> int:
        """Maximum number of columns to display in the TUI."""
        return self._x_len_max

    @x_len_max.setter
    def x_len_max(self, value: int) -> None:
        self._log(DEBUG, f"Setting x_len_max to {value}")
        if value == 0:
            value = self.x_max
        self._x_len_max: int = value

    @property
    def x_stop(self) -> int:
        """Ending column index for the TUI display."""
        return min(self.x_max, self.x_strt + self.x_len_max)

    @property
    def x_len(self) -> int:
        """Actual number of columns to display"""
        return self.x_stop - self.x_strt + 1

    @property
    def y_strt(self) -> int:
        """Starting row index for the TUI display."""
        return self._y_strt

    @y_strt.setter
    def y_strt(self, value: int) -> None:
        self._log(DEBUG, f"Setting y_strt to {value}")
        self._y_strt: int = value

    @property
    def y_len_max(self) -> int:
        """Maximum number of rows to display in the TUI."""
        return self._y_len_max

    @y_len_max.setter
    def y_len_max(self, value: int) -> None:
        self._log(DEBUG, f"Setting y_len_max to {value}")
        if value == 0:
            value = self.y_max
        self._y_len_max: int = value

    @property
    def y_stop(self) -> int:
        """Ending row index for the TUI display."""
        return min(self.y_max, self.y_strt + self.y_len_max)

    @property
    def y_len(self) -> int:
        """Actual number of rows to display"""
        return self.y_stop - self.y_strt

    def _message(self, message: str) -> str:
        """
        Formats a log message with a standard prefix.

        Args:
            message (str): Message to log.

        Returns:
            str: Formatted log message.
        """
        return f"[TUI Window Config] {message}"

    def _log(self, level: int, message: str) -> None:
        """
        Logs a message at the specified log level.

        Args:
            level (int): Log level.
            message (str): Message to log.
        """
        self._logger.log(level, self._message(message))

    def refresh_bounds(self) -> None:
        """Refreshes the terminal boundaries"""
        self.terminal_config.refresh_bounds()
