from base64 import b64encode
from collections.abc import Iterator
from http.client import HTTPResponse
from logging import DEBUG, Logger, getLogger
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json

from .constants import DEFAULT_PAGE_SIZE, ENDPOINT_SEARCH
from jira_cli.config import Config
from jira_cli.type_definitions import JSONObject


class JiraClient:
    """A client for interacting with the Jira API."""

    def __init__(
        self,
        base_url: str,
        api_token: str,
        email: str,
        logger: Logger = getLogger(__name__),
        page_size: int = DEFAULT_PAGE_SIZE,
    ) -> None:
        """
        Initializes a JiraClient instance.

        Args:
            base_url (str): Base URL for the Jira API.
            api_token (str): API token for authentication.
            email (str): Email address for authentication.
            logger (Logger): Logger instance.
            page_size (int): Number of items to fetch per page.
        """
        self._logger = logger
        self._log(DEBUG, "Initializing JiraClient instance")
        self.base_url = base_url
        self.api_token = api_token
        self.email = email
        self.page_size = page_size

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
        self.__logger: Logger = value

    @property
    def base_url(self) -> str:
        """Returns the base URL."""
        return self._base_url

    @base_url.setter
    def base_url(self, value: str) -> None:
        self._log(DEBUG, f"Setting base_url to: {value}")
        self._base_url: str = value

    @property
    def api_token(self) -> str:
        """Returns the API token."""
        return self._api_token

    @api_token.setter
    def api_token(self, value: str) -> None:
        self._log(DEBUG, f"Setting api_token to: {value}")
        self._api_token: str = value

    @property
    def email(self) -> str:
        """Returns the email."""
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        self._log(DEBUG, f"Setting email to: {value}")
        self._email: str = value

    @property
    def page_size(self) -> int:
        """Returns the page size."""
        return self._page_size

    @page_size.setter
    def page_size(self, value: int) -> None:
        self._log(DEBUG, f"Setting page_size to: {value}")
        self._page_size: int = value

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

    def _scroll(
        self,
        method: str,
        base_url: str,
        headers: dict[str, str],
        parameters: JSONObject,
    ) -> Iterator[JSONObject]:
        """
        Scrolls through paginated API responses.

        Args:
            method (str): HTTP method (e.g., "GET", "POST").
            base_url (str): Base URL for the API endpoint.
            headers (dict[str, str]): HTTP headers for the request.
            parameters (JSONObject): Query parameters for the request.

        Returns:
            Iterator[JSONObject]: An iterator over the paginated responses.
        """
        while True:
            url: str = f"{base_url}?{urlencode(parameters)}"
            request: Request = Request(method=method, url=url, headers=headers)
            self._log(DEBUG, f"Making request to URL: {url}")
            response: HTTPResponse = urlopen(request)
            # TODO: Improve handling
            data: JSONObject = json.loads(response.read().decode("utf-8"))
            yield data
            if data["isLast"]:
                self._log(DEBUG, "All tickets fetched, exiting loop")
                break
            parameters["nextPageToken"] = data["nextPageToken"]

    def list_issues(
        self,
        jql: str,
        fields: list[str] | None = None,
        limit: int = 0,
    ) -> Iterator[JSONObject]:
        """
        Lists issues for a given project using JQL search.

        Args:
            jql (str): JQL query string.
            fields (list[str] | None): List of fields to retrieve for each issue.
            limit (int): Maximum number of issues to retrieve. 0 means no limit. Defaults to 0.

        Returns:
            Iterator[JSONObject]: An iterator over the issues.
        """
        # TODO: Validate JQL
        self._log(DEBUG, "Fetching issues")
        headers: dict[str, str] = {
            "Authorization": f"Basic {self.auth_header}",
            "Accept": "application/json",
        }
        parameters: JSONObject = {"jql": jql, "maxResults": self.page_size}
        if fields is not None:
            parameters["fields"] = ",".join(fields)
            parameters["fieldsByKeys"] = True
        counter: int = 0
        for response in self._scroll(
            method="GET",
            base_url=f"{self.base_url}{ENDPOINT_SEARCH}",
            headers=headers,
            parameters=parameters,
        ):
            for issue in response["issues"]:
                yield issue
                counter += 1
                if limit > 0 and counter >= limit:
                    self._log(DEBUG, "Limit reached, exiting loop")
                    return
