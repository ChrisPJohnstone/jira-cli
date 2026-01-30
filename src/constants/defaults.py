from pathlib import Path
from typing import Final


DEFAULT_CONFIG_DIR: Final[Path] = Path.home() / ".config" / "jira_cli"
DEFAULT_CONFIG_FILE: Final[str] = "config.toml"
DEFAULT_CONFIG_PATH: Final[Path] = DEFAULT_CONFIG_DIR / DEFAULT_CONFIG_FILE
