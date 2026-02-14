from logging import DEBUG, Logger, getLogger
from pathlib import Path
from typing import Any
import tomllib
import json

from .type_definitions import ConfigRaw
from jira_cli.constants import DEFAULT_CONFIG_PATH


class Config:
    """Configuration class for application settings."""

    def __init__(
        self,
        jira_base_url: str,
        jira_api_token: str,
        jira_email: str,
        logger: Logger = getLogger(__name__),
    ) -> None:
        """
        Initializes the Config instance.

        Args:
            logger (Logger): Logger instance for logging.
        """
        self._logger = logger
        self._log(DEBUG, "Initializing Config instance")
        self.jira_base_url = jira_base_url
        self.jira_api_token = jira_api_token
        self.jira_email = jira_email

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
            jira_base_url=config_raw["jira_base_url"],
            jira_api_token=config_raw["jira_api_token"],
            jira_email=config_raw["jira_email"],
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
    def jira_base_url(self) -> str:
        """Returns the base URL."""
        return self._jira_base_url

    @jira_base_url.setter
    def jira_base_url(self, value: str) -> None:
        self._log(DEBUG, f"Setting jira_base_url to: {value}")
        if value.endswith("/"):
            self._log(DEBUG, "Removing trailing slash from jira_base_url")
            value = value.removesuffix("/")
        self._jira_base_url = value

    @property
    def jira_api_token(self) -> str:
        """Returns the API token."""
        return self._jira_api_token

    @jira_api_token.setter
    def jira_api_token(self, value: str) -> None:
        self._log(DEBUG, "Setting jira_api_token")
        self._jira_api_token = value

    @property
    def jira_email(self) -> str:
        """Returns the Jira email."""
        return self._jira_email

    @jira_email.setter
    def jira_email(self, value: str) -> None:
        self._log(DEBUG, f"Setting jira_email to: {value}")
        self._jira_email = value

    def __str__(self) -> str:
        """
        A string representation of the configuration.

        Returns:
            str: String representation of the configuration.
        """
        return json.dumps(self.to_dict(), indent=2)

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

    def to_dict(self) -> dict[str, Any]:
        """
        Converts the configuration to a dictionary.

        Returns:
            dict[str, str]: Configuration as a dictionary.
        """
        return {
            "jira_base_url": self.jira_base_url,
            "jira_api_token": "*" * len(self.jira_api_token),
            "jira_email": self.jira_email,
        }
