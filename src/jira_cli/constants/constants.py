from typing import Final

from .defaults import DEFAULT_CONFIG_PATH


CONFIG_PATH_ARG_NAME: Final[str] = "config-path"
CONFIG_PATH_DEST: Final[str] = "config_path"
CONFIG_PATH_ARG_HELP_STR: Final[str] = (
    f"Path to the configuration file. Default: {DEFAULT_CONFIG_PATH}"
)
