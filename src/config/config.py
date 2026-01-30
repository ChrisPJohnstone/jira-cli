from logging import Logger, getLogger
from pathlib import Path
import tomllib

from .type_definitions import ConfigRaw
from constants import DEFAULT_CONFIG_PATH


class Config:
    """Configuration class for application settings."""

    def __init__(
        self,
        logger: Logger = getLogger(__name__),
    ) -> None:
        pass

    @classmethod
    def from_path(
        cls: type[Config],
        path: Path = DEFAULT_CONFIG_PATH,
        logger: Logger = getLogger(__name__),
    ) -> Config:
        if not path.exists():
            raise FileNotFoundError(f"Config does not exist at {path}.")
        if not path.is_file():
            raise IsADirectoryError(f"Config {path} is not a file.")
        config_raw: ConfigRaw = tomllib.loads(path.read_text())  # type: ignore[assignment]
        print(config_raw)
        return cls(logger=logger)
