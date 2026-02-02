import json

from jira_cli.type_definitions import JSONObject


def write_output(data: JSONObject) -> None:
    """
    Writes the given data as a JSON string to standard output.

    Args:
        data (JSONObject): The data to write.
    """
    output: str = json.dumps(data)
    print(output)
