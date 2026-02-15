from logging import DEBUG, Logger, getLogger

from ..utils import terminal_height, terminal_width


class ConfigTerminal:
    """Configuration class for terminal dimensions"""

    def __init__(
        self,
        logger: Logger = getLogger(__name__),
    ) -> None:
        """
        Initializes the Config instance.

        Args:
            logger (Logger): Logger instance for logging.
        """
        self._logger = logger
        self.refresh_bounds()

    @property
    def _logger(self) -> Logger:
        return self.__logger

    @_logger.setter
    def _logger(self, value: Logger) -> None:
        self.__logger: Logger = value

    @property
    def x_max(self) -> int:
        """Maximum number of columns in the terminal."""
        return self._x_max

    @x_max.setter
    def x_max(self, value: int) -> None:
        self._log(DEBUG, f"Setting x_max to {value}")
        self._x_max: int = value

    @property
    def y_max(self) -> int:
        """Maximum number of rows in the terminal."""
        return self._y_max

    @y_max.setter
    def y_max(self, value: int) -> None:
        self._log(DEBUG, f"Setting y_max to {value}")
        self._y_max: int = value

    def _message(self, message: str) -> str:
        """
        Formats a log message with a standard prefix.

        Args:
            message (str): Message to log.

        Returns:
            str: Formatted log message.
        """
        return f"[TUI Config] {message}"

    def _log(self, level: int, message: str) -> None:
        """
        Logs a message at the specified log level.

        Args:
            level (int): Log level.
            message (str): Message to log.
        """
        self._logger.log(level, self._message(message))

    def refresh_x_max(self) -> None:
        """Sets x_max based on the current terminal size."""
        self._log(DEBUG, "Refreshing x_max")
        self.x_max = terminal_width() - 1

    def refresh_y_max(self) -> None:
        """Sets y_max based on the current terminal size."""
        self._log(DEBUG, "Refreshing y_max")
        self.y_max = terminal_height()

    def refresh_bounds(self) -> None:
        """Refreshes the terminal boundaries"""
        self._log(DEBUG, "Refreshing terminal bounds")
        self.refresh_x_max()
        self.refresh_y_max()
