from argparse import Namespace

from jira_cli.config import Config
from jira_cli.jira_client import JiraClient
from jira_cli.tui import ConfigWindow, TUIClient, WindowIssue


def main(args: Namespace) -> None:
    """
    Lists all tickets.

    Args:
        args (Namespace): Parsed command-line arguments.
    """
    config: Config = Config.from_path(args.config_path, args.logger)
    jira_client: JiraClient = JiraClient.from_config(config, args.logger)
    tui: TUIClient = TUIClient(args.logger)
    window_config: ConfigWindow = tui.window_config()
    window_issue: WindowIssue = WindowIssue(window_config, jira_client, args.id)
    tui.init(window_issue)
