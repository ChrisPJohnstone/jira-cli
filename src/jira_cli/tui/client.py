from curses import KEY_RESIZE, curs_set, window, wrapper
from logging import DEBUG, Logger, getLogger

from .config import ConfigTerminal, ConfigWindow
from .constants import Action
from .windows import Window


class TUIClient:
    def __init__(self, logger: Logger = getLogger(__name__)) -> None:
        """
        Initializes the TUIClient instance.

        Args:
            logger (Logger): Logger instance for logging.
        """
        self._logger = logger
        self.terminal_config = ConfigTerminal(logger)

    @property
    def _logger(self) -> Logger:
        return self.__logger

    @_logger.setter
    def _logger(self, value: Logger) -> None:
        self.__logger: Logger = value

    @property
    def terminal_config(self) -> ConfigTerminal:
        """TerminalConfig instance for accessing terminal dimensions."""
        return self._terminal_config

    @terminal_config.setter
    def terminal_config(self, value: ConfigTerminal) -> None:
        self._log(DEBUG, "Setting Terminal Config")
        self._terminal_config: ConfigTerminal = value

    @property
    def windows(self) -> list[Window]:
        """Stack of active windows in the TUI."""
        return self._windows

    @windows.setter
    def windows(self, value: list[Window]) -> None:
        self._log(DEBUG, "Setting windows")
        self._windows: list[Window] = value

    @property
    def active_window(self) -> Window:
        """Returns the currently active window."""
        return self.windows[0]

    def _message(self, message: str) -> str:
        """
        Formats a log message with a standard prefix.

        Args:
            message (str): Message to log.

        Returns:
            str: Formatted log message.
        """
        return f"[TUI Client] {message}"

    def _log(self, level: int, message: str) -> None:
        """
        Logs a message at the specified log level.

        Args:
            level (int): Log level.
            message (str): Message to log.
        """
        self._logger.log(level, self._message(message))

    def window_config(
        self,
        x_strt: int = 0,
        y_strt: int = 0,
        x_len_max: int = 0,
        y_len_max: int = 0,
    ) -> ConfigWindow:
        """
        Returns a WindowConfig isntance with the specified parameters.

        Args:
            x_strt (int): Starting column index for the window.
            y_strt (int): Starting row index for the window.
            x_len_max (int): Maximum height of the window.
            y_len_max (int): Maximum width of the window.
        """
        return ConfigWindow(
            terminal_config=self.terminal_config,
            x_strt=x_strt,
            y_strt=y_strt,
            x_len_max=x_len_max,
            y_len_max=y_len_max,
        )

    def _resize(self, screen: window) -> None:
        """Handles terminal resize events."""
        for win in self.windows[::-1]:
            win.refresh_bounds()
            win.draw(screen)

    def _quit_window(self) -> None:
        """
        Closes the currently active window and returns to the previous one.

        If there are no more windows, the TUI will exit.
        """
        self.windows.pop(0)

    def _quit(self) -> None:
        """Closes all windows and exits the TUI."""
        self.windows.clear()

    def handle_input(self, screen: window) -> None:
        """
        Handles user input and triggers the corresponding actions.

        Args:
            screen (window): Curses window object for the main screen.
        """
        key: int = screen.getch()
        self._log(DEBUG, f"Key {key} pressed")
        if key == KEY_RESIZE:
            return self._resize(screen)
        if key not in self.active_window.BINDINGS:
            return
        action: Action = self.active_window.BINDINGS[key]
        if action is Action.QUIT:
            return self._quit_window()
        self.active_window.action(action)

    def main(self, stdscr: window) -> None:
        """
        Main loop for the TUI.

        Args:
            stdscr (window): Curses window object for the main screen.
        """
        curs_set(0)
        stdscr.refresh()
        while self.windows:
            self.active_window.draw(stdscr)
            self.handle_input(stdscr)

    def init(self, start_window: Window) -> None:
        """Initializes TUI and starts the main loop."""
        self.windows = [start_window]
        wrapper(self.main)
