from argparse import Namespace

from config import Config
from jira_client import JiraClient


def main(args: Namespace) -> None:
    """
    Lists all tickets.

    Args:
        args (Namespace): Parsed command-line arguments.
    """
    config: Config = Config.from_path(
        path=args.config_path,
        logger=args.logger,
    )
    jira_client: JiraClient = JiraClient.from_config(config, args.logger)
    jira_client.authenticate()
