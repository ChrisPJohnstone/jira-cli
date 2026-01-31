from logging import DEBUG, Logger, getLogger

from config import Config


class JiraClient:
    """A client for interacting with the Jira API."""

    def __init__(
        self,
        base_url: str,
        api_token: str,
        logger: Logger = getLogger(__name__),
    ) -> None:
        """
        Initializes a JiraClient instance.

        Args:
            base_url (str): Base URL for the Jira API.
            api_token (str): API token for authentication.
            logger (Logger): Logger instance.
        """
        self._logger = logger
        self._log(DEBUG, "Initializing JiraClient instance")
        self.base_url = base_url
        self.api_token = api_token

    @classmethod
    def from_config(
        cls: type[JiraClient],
        config: Config,
        logger: Logger = getLogger(__name__),
    ) -> JiraClient:
        """
        Creates a JiraClient instance from a Config object.

        Args:
            config (Config): Configuration object.
            logger (Logger): Logger instance.

        Returns:
            JiraClient: JiraClient instance.
        """
        return cls(
            base_url=config.jira_base_url,
            api_token=config.jira_api_token,
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

    def authenticate(self) -> None:
        raise NotImplementedError("'authenticate' is not implemented yet.")
