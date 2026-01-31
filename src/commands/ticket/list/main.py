from argparse import Namespace

from config import Config
from jira_client import JiraClient
from type_definitions import JSONObject


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
    for issue in jira_client.list_issues(
        jql=args.jql,
        fields=["summary"],
        limit=10,
        # TODO: Move to arg parser
    ):
        key: str = issue["key"]
        fields: JSONObject = issue["fields"]
        print(f"{key}: {fields['summary']}")
