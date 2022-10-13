import enum
import os
from dataclasses import dataclass, fields, MISSING

import toml


class LogLevel(str, enum.Enum):  # noqa: WPS600
    """Possible log levels."""

    NOTSET = "NOTSET"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FATAL = "FATAL"


@dataclass
class InfoSettings:
    """Settings for the app."""

    name: str = 'App'
    description: str = 'This is app'
    version: str = '0.1.0'


@dataclass
class ApiSettings:
    """Settings for the API server."""

    host: str = "127.0.0.1"
    port: int = 8000
    workers_count: int = 1
    reload: bool = False


@dataclass
class DatabaseSettings:
    """Settings for the database."""

    models: list[str]

    protocol: str = "sqlite"
    file_name: str = "production-database.sqlite3"
    user: str = None
    password: str = None
    host: str = None
    port: int = None

    def get_db_url(self):
        if self.protocol == "sqlite":
            return f"{self.protocol}://{self.file_name}"
        return f"{self.protocol}://{self.user}:{self.password}@{self.host}:{self.port}"

    def get_tortoise_config(self):
        return {
            "connections": {"default": self.get_db_url()},
            "apps": {
                "models": {
                    "models": self.models,
                    "default_connection": "default",
                },
            },
        }


@dataclass
class Settings:
    """Application settings."""

    api: ApiSettings
    info: InfoSettings
    database: DatabaseSettings

    @property
    def log_level(self):
        return LogLevel.INFO

    @classmethod
    def from_env(cls, data: dict) -> "Settings":
        """Create settings from environment variables."""

        sections = {}

        for section in fields(cls):
            pre = {}
            current = data[section.name]

            for field in fields(section.type):
                if field.name in current:
                    pre[field.name] = current[field.name]
                elif field.default is not MISSING:
                    pre[field.name] = field.default
                else:
                    raise ValueError(
                        f"Missing field {field.name} in section {section.name}"
                    )

            sections[section.name] = section.type(**pre)

        return cls(**sections)


def get_settings(config_file: str) -> Settings:
    """Get settings from the config file."""

    if not os.path.isfile(config_file):
        raise FileNotFoundError(f"Config file not found: {config_file} no such file")

    with open(config_file, "r") as f:
        data = toml.load(f)

    return Settings.from_env(data)
