from argparse import ArgumentParser
from typing import Protocol

from .subcommands_property import SubCommandsProperty


class CommandModule(Protocol):
    SUBCOMMANDS: SubCommandsProperty

    @staticmethod
    def command_parsers() -> list[ArgumentParser]: ...
