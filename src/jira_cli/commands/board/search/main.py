from argparse import Namespace
import json

from jira_cli.config import Config
from jira_cli.jira_client import JiraClient, SearchBoardsArgs


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
    kwargs: SearchBoardsArgs = {"limit": args.limit}
    if hasattr(args, "project"):
        kwargs["project"] = args.project
    for board in jira_client.search_boards(**kwargs):
        # TODO: Add args for method params
        print(json.dumps(board))
