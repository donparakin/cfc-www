import os
import tomllib
from pathlib import Path

_unspecified = object()


class SettingsFromTOML:
    """
    Settings from a TOML file
    - Intended for environment specific settings (prod, dev, etc)
    - Reads from a TOML formatted file  (see https://toml.io)
    - Location of the TOML file is in an environment variable.
    - get() gets values using dot-delimited keys. Example:
      get("django.DEBUG") returns settings["django"]["DEBUG"].
    - TOML is good because when read it converts values to Python
      primitives such as string, int, float, lists, dict.
    """

    def __init__(self, env_var: str, base_dir: Path = None):
        self.base_dir = base_dir
        if env_var not in os.environ:
            raise RuntimeError(f'Environment var "{env_var}" must be set.')
        self.fpath = Path(os.environ[env_var]).resolve()
        if not self.fpath.exists():
            raise FileNotFoundError(f'"{env_var}" file not found: {self.fpath}')
        if not self.fpath.is_file():
            raise FileNotFoundError(f'"{env_var}" file is not a file: {self.fpath}')
        with open(self.fpath, "rb") as f:
            self.settings = tomllib.load(f)

    def get(self, key: str, default=_unspecified) -> any:
        """
        For the given key, return a settings value.
        - Keys are dot-delimited strings. Example: "django.DEBUG"
          will return settings["django"]["DEBUG"].
        - If not found, returns default or raises a KeyError
        :param key: dot-delimited key
        :param default: returned if key is not found
        """
        keys = str(key).split(".")
        value = self.settings
        for k in keys:
            if k in value:
                value = value[k]
            elif default is _unspecified:
                raise KeyError(f'Setting "{key}" not found in {self.fpath}')
            else:
                return default
        if self.base_dir and isinstance(value, str):
            value = value.replace("{{BASE_DIR}}", str(self.base_dir))
        return value
