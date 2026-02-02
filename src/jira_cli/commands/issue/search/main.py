from argparse import Namespace

from jira_cli.config import Config
from jira_cli.jira_client import JiraClient
from jira_cli.utils import write_output


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
    for issue in jira_client.search_issues(
        jql=args.jql,
        fields=["summary"],
        limit=args.limit,
        # TODO: Move to arg parser
    ):
        write_output(issue)
