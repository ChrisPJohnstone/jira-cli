from argparse import Namespace

from jira_cli.config import Config
from jira_cli.jira_client import ArgsSearchBoards, JiraClient
from jira_cli.utils import write_output


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
    kwargs: ArgsSearchBoards = {"limit": args.limit}
    if hasattr(args, "project"):
        kwargs["project"] = args.project
    if hasattr(args, "board_type"):
        kwargs["board_type"] = args.board_type
    for board in jira_client.search_boards(**kwargs):
        # TODO: Add args for method params
        write_output(board)
