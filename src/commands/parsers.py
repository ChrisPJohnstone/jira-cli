from argparse import ArgumentParser

from parsers import log_level


def shared_parsers() -> list[ArgumentParser]:
    return [log_level()]
