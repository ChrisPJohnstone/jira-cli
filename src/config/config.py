from logging import DEBUG, Logger, getLogger
from pathlib import Path
from typing import Any
import tomllib
import json

from .type_definitions import ConfigRaw
from constants import DEFAULT_CONFIG_PATH


class Config:
    """Configuration class for application settings."""

    def __init__(
        self,
        base_url: str,
        api_token: str,
        logger: Logger = getLogger(__name__),
    ) -> None:
        """
        Initializes the Config instance.

        Args:
            logger (Logger): Logger instance for logging.
        """
        self._logger = logger
        self._log(DEBUG, "Initializing Config instance")
        self.base_url = base_url
        self.api_token = api_token

    @classmethod
    def from_path(
        cls: type[Config],
        path: Path | None = None,
        logger: Logger = getLogger(__name__),
    ) -> Config:
        """
        Loads configuration from the specified file path.

        Args:
            path (Path): Path to the configuration file.
            logger (Logger): Logger instance for logging.

        Returns:
            Config: Loaded configuration instance.
        """
        _path: Path = path or DEFAULT_CONFIG_PATH
        logger.debug(f"Loading config from path: {_path}")
        if not _path.exists():
            raise FileNotFoundError(f"Config does not exist at {_path}.")
        if not _path.is_file():
            raise IsADirectoryError(f"Config {_path} is not a file.")
        config_raw: ConfigRaw = tomllib.loads(_path.read_text())  # type: ignore[assignment]
        logger.debug("Config loaded succesfully")
        return cls(
            base_url=config_raw["base_url"],
            api_token=config_raw["api_token"],
            logger=logger,
        )

    @property
    def _logger(self) -> Logger:
        """Returns the logger instance."""
        return self.__logger

    @_logger.setter
    def _logger(self, value: Logger) -> None:
        self.__logger = value

    @property
    def base_url(self) -> str:
        """Returns the base URL."""
        return self._base_url

    @base_url.setter
    def base_url(self, value: str) -> None:
        self._log(DEBUG, f"Setting base_url to: {value}")
        self._base_url = value

    @property
    def api_token(self) -> str:
        """Returns the API token."""
        return self._api_token

    @api_token.setter
    def api_token(self, value: str) -> None:
        self._log(DEBUG, f"Setting api_token to: {value}")
        self._api_token = value

    def __str__(self) -> str:
        """
        A string representation of the configuration.

        Returns:
            str: String representation of the configuration.
        """
        config_dict: dict[str, Any] = {
            "base_url": self.base_url,
            "api_token": self.api_token,
        }
        return json.dumps(config_dict, indent=2)

    def _message(self, message: str) -> str:
        """
        Formats a log message with a standard prefix.

        Args:
            message (str): Message to log.

        Returns:
            str: Formatted log message.
        """
        return f"[Config] {message}"

    def _log(self, level: int, message: str) -> None:
        """
        Logs a message at the specified log level.

        Args:
            level (int): Log level.
            message (str): Message to log.
        """
        self._logger.log(level, self._message(message))
