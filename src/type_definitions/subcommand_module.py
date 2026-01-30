from argparse import ArgumentParser
from typing import Protocol


class SubCommandModule(Protocol):
    @staticmethod
    def command_parsers() -> list[ArgumentParser]: ...
