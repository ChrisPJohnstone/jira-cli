from argparse import Namespace
import json

from jira_cli.config import Config
from jira_cli.jira_client import JiraClient


def main(args: Namespace) -> None:
    """
    Lists all boards.

    Args:
        args (Namespace): Parsed command-line arguments.
    """
    config: Config = Config.from_path(
        path=args.config_path,
        logger=args.logger,
    )
    jira_client: JiraClient = JiraClient.from_config(config, args.logger)
    for board in jira_client.list_boards(limit=args.limit):
        # TODO: Add args for method params
        print(json.dumps(board))
