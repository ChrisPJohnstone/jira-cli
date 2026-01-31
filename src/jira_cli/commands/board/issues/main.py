from argparse import Namespace
import json

from jira_cli.config import Config
from jira_cli.jira_client import ArgsSearchBoardIssues, JiraClient


def main(args: Namespace) -> None:
    """
    Lists all issues for board.

    Args:
        args (Namespace): Parsed command-line arguments.
    """
    config: Config = Config.from_path(
        path=args.config_path,
        logger=args.logger,
    )
    jira_client: JiraClient = JiraClient.from_config(config, args.logger)
    kwargs: ArgsSearchBoardIssues = {
        "board_id": args.id,
        "limit": args.limit,
    }
    if hasattr(args, "jql"):
        kwargs["jql"] = args.jql
    for board in jira_client.search_board_issues(**kwargs):
        # TODO: Add args for method params
        print(json.dumps(board))
