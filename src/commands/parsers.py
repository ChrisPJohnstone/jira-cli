from argparse import ArgumentParser

from constants import CONFIG_PATH_ARG_NAME, CONFIG_PATH_ARG_HELP_STR
from parsers import log_level, path


def shared_parsers() -> list[ArgumentParser]:
    return [
        path(
            arg_name=CONFIG_PATH_ARG_NAME,
            help_str=CONFIG_PATH_ARG_HELP_STR,
        ),
        log_level(),
    ]
