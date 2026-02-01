from argparse import Namespace
from pathlib import Path
from typing import Final
from unittest.mock import MagicMock, patch

from jira_cli.constants import (
    CONFIG_PATH_ARG_NAME,
    DEFAULT_CONFIG_PATH,
    DEFAULT_LOG_LEVEL,
)
from jira_cli.cli import main
from test_utils import TestSet, parametrize

FILEPATH: Final[str] = "jira_cli.cli"
COMMAND_PATH: Final[str] = "jira_cli.commands"
COMMAND: Final[str] = "jira"


main_cases: TestSet = {
    "board issues defaults": {
        "expected_main": f"{COMMAND_PATH}.board.issues.main",
        "argv": [COMMAND, "board", "issues", "--id", "123"],
        "expected_args": Namespace(
            config_path=DEFAULT_CONFIG_PATH,
            id=123,
            jql=None,
            limit=10,
        ),
        "expected_log_level": DEFAULT_LOG_LEVEL,
    },
    "board issues values": {
        "expected_main": f"{COMMAND_PATH}.board.issues.main",
        "argv": [
            COMMAND,
            "board",
            "issues",
            "--id",
            "456",
            "--jql",
            "status=Done",
            "--limit",
            "20",
            f"--{CONFIG_PATH_ARG_NAME}",
            "/another/path",
            "--log-level",
            "30",
        ],
        "expected_args": Namespace(
            config_path=Path("/another/path"),
            id=456,
            jql="status=Done",
            limit=20,
            log_level=30,
        ),
        "expected_log_level": 30,
    },
    "board list defaults": {
        "expected_main": f"{COMMAND_PATH}.board.search.main",
        "argv": [COMMAND, "board", "list"],
        "expected_args": Namespace(config_path=DEFAULT_CONFIG_PATH, limit=10),
        "expected_log_level": DEFAULT_LOG_LEVEL,
    },
    "board list values": {
        "expected_main": f"{COMMAND_PATH}.board.search.main",
        "argv": [
            COMMAND,
            f"--{CONFIG_PATH_ARG_NAME}",
            "/custom/path",
            "board",
            "--log-level",
            "10",
            "list",
            "--limit",
            "5",
        ],
        "expected_args": Namespace(
            config_path=Path("/custom/path"),
            limit=5,
            log_level=10,
        ),
        "expected_log_level": 10,
    },
    "config show defaults": {
        "expected_main": f"{COMMAND_PATH}.config.show.main",
        "argv": [COMMAND, "config", "show"],
        "expected_args": Namespace(config_path=DEFAULT_CONFIG_PATH),
        "expected_log_level": DEFAULT_LOG_LEVEL,
    },
    "config show values": {
        "expected_main": f"{COMMAND_PATH}.config.show.main",
        "argv": [
            COMMAND,
            "--log-level",
            "20",
            "config",
            f"--{CONFIG_PATH_ARG_NAME}",
            "/etc/jira_cli/config.toml",
            "show",
        ],
        "expected_args": Namespace(
            config_path=Path("/etc/jira_cli/config.toml"),
            log_level=20,
        ),
        "expected_log_level": 20,
    },
    "issue list defaults": {
        "expected_main": f"{COMMAND_PATH}.issue.search.main",
        "argv": [COMMAND, "issue", "list", "--jql", "assignee=currentUser()"],
        "expected_args": Namespace(
            config_path=DEFAULT_CONFIG_PATH,
            jql="assignee=currentUser()",
            limit=10,
        ),
        "expected_log_level": DEFAULT_LOG_LEVEL,
    },
    "issue list values": {
        "expected_main": f"{COMMAND_PATH}.issue.search.main",
        "argv": [
            COMMAND,
            f"--{CONFIG_PATH_ARG_NAME}",
            "/home/user/jira_config.toml",
            "--log-level",
            "40",
            "issue",
            "list",
            "--jql",
            "project=TEST",
            "--limit",
            "15",
        ],
        "expected_args": Namespace(
            config_path=Path("/home/user/jira_config.toml"),
            jql="project=TEST",
            limit=15,
            log_level=40,
        ),
        "expected_log_level": 40,
    },
}


@patch(f"{FILEPATH}.getLogger")
@parametrize(main_cases)
def test_main(
    mock_get_logger: MagicMock,
    expected_main: str,
    argv: list[str],
    expected_args: Namespace,
    expected_log_level: int,
) -> None:
    with (
        patch("sys.argv", argv),
        patch(expected_main) as mock_args_main,
    ):
        mock_logger: MagicMock = mock_get_logger.return_value
        expected_args.main = mock_args_main
        expected_args.logger = mock_logger
        main()
        mock_args_main.assert_called_once_with(expected_args)
    mock_logger.setLevel.assert_called_once_with(level=expected_log_level)
