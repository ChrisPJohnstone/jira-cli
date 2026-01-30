from argparse import ArgumentParser
from typing import Final

from parsers import path


PATH_HELP_STR: Final[str] = "Path to the configuration file."


def command_parsers() -> list[ArgumentParser]:
    return [
        path(help_str=PATH_HELP_STR),
    ]
