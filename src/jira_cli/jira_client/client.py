from base64 import b64encode
from collections.abc import Iterator
from http.client import HTTPResponse
from logging import DEBUG, Logger, getLogger
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json

from .constants import (
    APIVersion,
    BoardType,
    DEFAULT_PAGE_SIZE,
    Endpoint,
)
from .type_definitions import RequestKwargs
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
        self._log(DEBUG, "Setting api_token")
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
        return f"[Jira Client] {message}"

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

    def _request(
        self,
        method: str,
        url: str,
        headers: dict[str, str] | None = None,
        body: JSONObject | None = None,
    ) -> HTTPResponse:
        """Make an HTTP request.

        Args:
            method: The HTTP method to use.
            url: The URL to send the request to.
            headers: The headers to include in the request.
            body: The body of the request.

        Returns:
            The HTTP response.
        """
        kwargs: RequestKwargs = {"method": method, "url": url}
        if headers:
            kwargs["headers"] = headers
        if body:
            if method == "GET":
                kwargs["url"] += f"?{urlencode(body)}"
            else:
                kwargs["data"] = json.dumps(body).encode("utf-8")
        self._log(DEBUG, f"Making request with kwargs: {kwargs}")
        request: Request = Request(**kwargs)
        return urlopen(request)

    def get_results(
        self,
        method: str,
        api_version: APIVersion,
        endpoint: str,
        headers: dict[str, str],
        body: JSONObject,
        is_pagination: bool = False,
    ) -> Iterator[JSONObject]:
        """
        Scrolls through paginated API responses.

        Args:
            method (str): HTTP method (e.g., "GET", "POST").
            api_version (APIVersion): API version to use.
            endpoint (str): API endpoint to call.
            headers (dict[str, str]): HTTP headers for the request.
            body (JSONObject): Body for the request.
            is_pagination (bool): Whether to handle pagination. Defaults to False.

        Returns:
            Iterator[JSONObject]: An iterator over the paginated responses.
        """
        base_url: str = f"{self.base_url}{api_version}{endpoint}"
        while True:
            response: HTTPResponse = self._request(
                method=method,
                url=base_url,
                headers=headers,
                body=body,
            )
            data: JSONObject = json.loads(response.read().decode("utf-8"))
            yield data
            if not is_pagination:
                self._log(DEBUG, "Pagination disabled, exiting loop")
                return
            # TODO: Move pagination logic to separate method
            match api_version:
                case APIVersion.CLOUD:
                    if data["isLast"]:
                        self._log(DEBUG, "All pages fetched, exiting loop")
                        return
                    body["nextPageToken"] = data["nextPageToken"]
                case APIVersion.SOFTWARE_CLOUD:
                    body["startAt"] = data["startAt"] + data["maxResults"]
                case _:
                    raise NotImplementedError(
                        f"Pagination not implemented for API version: {api_version}"
                    )

    def parse_jql(self, jql: str) -> None:
        """
        Parses a JQL query string into a JSON object.

        Args:
            jql (str): JQL query string.

        Raises:
            ValueError: If there are errors in the JQL query.
        """
        self._log(DEBUG, "Parsing JQL query")
        headers: dict[str, str] = {
            "Authorization": f"Basic {self.auth_header}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        query: dict[str, str] = {"validation": "strict"}
        # TODO: Support validation arg
        # TODO: Maybe move handling query to `get_results` method
        body: JSONObject = {"queries": [jql]}
        for response in self.get_results(
            method="POST",
            api_version=APIVersion.CLOUD,
            endpoint=f"{Endpoint.JQL_PARSE}?{urlencode(query)}",
            headers=headers,
            body=body,
        ):
            query: JSONObject = response["queries"][0]
            if "errors" in query:
                raise ValueError(f"JQL parsing errors: {query['errors']}")

    def search_issues(
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
        self._log(DEBUG, "Fetching issues")
        self.parse_jql(jql)
        headers: dict[str, str] = {
            "Authorization": f"Basic {self.auth_header}",
            "Accept": "application/json",
        }
        body: JSONObject = {"jql": jql, "maxResults": self.page_size}
        if fields is not None:
            body["fields"] = ",".join(fields)
            body["fieldsByKeys"] = True
        counter: int = 0
        for response in self.get_results(
            method="GET",
            api_version=APIVersion.CLOUD,
            endpoint=Endpoint.SEARCH_JQL,
            headers=headers,
            body=body,
            is_pagination=True,
        ):
            for issue in response["issues"]:
                yield issue
                counter += 1
                if limit > 0 and counter >= limit:
                    self._log(DEBUG, "Limit reached, exiting loop")
                    return

    def search_boards(
        self,
        board_type: BoardType | None = None,
        name: str | None = None,
        project: str | None = None,
        limit: int = 0,
    ) -> Iterator[JSONObject]:
        """
        Lists dashboards.

        Args:
            board_type (BoardType | None): Type of board to filter dashboards. Defaults to None.
            name (str | None): Filters results to boards that match or partially match the specified name.
            project (str | None): Project key or ID to filter dashboards. Defaults to None.
            limit (int): Maximum number of dashboards to retrieve. 0 means no limit. Defaults to 0.

        Returns:
            Iterator[JSONObject]: An iterator over the dashboards.
        """
        self._log(DEBUG, "Fetching dashboards")
        headers: dict[str, str] = {
            "Authorization": f"Basic {self.auth_header}",
            "Accept": "application/json",
        }
        body: JSONObject = {"maxResults": self.page_size}
        if name is not None:
            body["name"] = name
        if board_type is not None:
            body["type"] = board_type
        if project is not None:
            body["projectKeyOrId"] = project
        counter: int = 0
        for response in self.get_results(
            method="GET",
            api_version=APIVersion.SOFTWARE_CLOUD,
            endpoint=Endpoint.SEARCH_BOARD,
            headers=headers,
            body=body,
            is_pagination=True,
        ):
            dashboards: list[JSONObject] = response["values"]
            if len(dashboards) == 0:
                self._log(DEBUG, "No more dashboards found, exiting loop")
                return
            for dashboard in dashboards:
                yield dashboard
                counter += 1
                if limit > 0 and counter >= limit:
                    self._log(DEBUG, "Limit reached, exiting loop")
                    return

    def search_board_issues(
        self,
        board_id: int,
        jql: str | None = None,
        limit: int = 0,
    ) -> Iterator[JSONObject]:
        """
        Lists all issues for a given board.

        Args:
            board_id (int): ID of the board.
            jql (str | None): JQL query string to filter issues. Defaults to None.
            limit (int): Maximum number of issues to retrieve. 0 means no limit. Defaults to 0.

        Returns:
            Iterator[JSONObject]: An iterator over the issues.
        """
        self._log(DEBUG, f"Fetching issues for board ID: {board_id}")
        body: JSONObject = {"maxResults": self.page_size}
        if jql is not None:
            self.parse_jql(jql)
            body["jql"] = jql
        headers: dict[str, str] = {
            "Authorization": f"Basic {self.auth_header}",
            "Accept": "application/json",
        }
        counter: int = 0
        for response in self.get_results(
            method="GET",
            api_version=APIVersion.SOFTWARE_CLOUD,
            endpoint=Endpoint.SEARCH_BOARD_ISSUES.format(board_id=board_id),
            headers=headers,
            body=body,
            is_pagination=True,
        ):
            issues: list[JSONObject] = response["issues"]
            if len(issues) == 0:
                self._log(DEBUG, "No more issues found, exiting loop")
                return
            for issue in issues:
                yield issue
                counter += 1
                if limit > 0 and counter >= limit:
                    self._log(DEBUG, "Limit reached, exiting loop")
                    return
