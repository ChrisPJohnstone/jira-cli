from base64 import b64encode
from http.client import HTTPResponse
from logging import DEBUG, Logger, getLogger
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json

from .constants import ENDPOINT_SEARCH
from config import Config


class JiraClient:
    """A client for interacting with the Jira API."""

    def __init__(
        self,
        base_url: str,
        api_token: str,
        email: str,
        logger: Logger = getLogger(__name__),
    ) -> None:
        """
        Initializes a JiraClient instance.

        Args:
            base_url (str): Base URL for the Jira API.
            api_token (str): API token for authentication.
            email (str): Email address for authentication.
            logger (Logger): Logger instance.
        """
        self._logger = logger
        self._log(DEBUG, "Initializing JiraClient instance")
        self.base_url = base_url
        self.api_token = api_token
        self.email = email

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
            email=config.jira_email,
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

    @property
    def email(self) -> str:
        """Returns the email."""
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        self._log(DEBUG, f"Setting email to: {value}")
        self._email = value

    @property
    def auth_header(self) -> str:
        """Returns the Auth header value."""
        # TODO: Support other auth methods
        if not hasattr(self, "_auth_header"):
            self._auth_header: str = self._basic_auth_header()
        return self._auth_header

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

    def _basic_auth_header(self) -> str:
        """
        Generates the Basic Auth header value.

        Returns:
            str: Base64 encoded auth string for Basic Auth.
        """
        auth_string: str = f"{self.email}:{self.api_token}"
        auth_bytes: bytes = auth_string.encode("ascii")
        base64_bytes: bytes = b64encode(auth_bytes)
        return base64_bytes.decode("ascii")

    def list_tickets(self) -> None:
        """
        Lists tickets for a given project using JQL search.

        Args:
            project (str): Project key to search for. Defaults to "MDATA".

        Returns:
            list[dict[str, Any]]: List of ticket/issue dictionaries.
        """
        # TODO: Parametrize method
        self._log(DEBUG, "Fetching tickets")
        params: dict[str, str] = {"jql": "project = MDATA"}
        url: str = f"{self.base_url}{ENDPOINT_SEARCH}?{urlencode(params)}"
        headers: dict[str, str] = {
            "Authorization": f"Basic {self.auth_header}",
            "Accept": "application/json",
        }
        request: Request = Request(method="GET", url=url, headers=headers)
        response: HTTPResponse = urlopen(request)
        response_data: str = response.read().decode("utf-8")
        data: dict[str, Any] = json.loads(response_data)
        # TODO: Improve type hint
        issues: list[dict[str, Any]] = data.get("issues", [])
        # TODO: Improve type hint
        for issue in issues:
            print(issue)
