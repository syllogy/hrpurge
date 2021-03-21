# -*- coding: utf-8 -*-

from dataclasses import dataclass
import logging
from typing import Callable
import coloredlogs

from hrpurge.log_handlers import BaseStreamHandler, BaseRichHandler, ContextHandler


class SingletonLogger(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                SingletonLogger, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


@dataclass
class Log(metaclass=SingletonLogger):
    log_level: str
    log_type: str
    logger_name: str

    def __post_init__(self):
        self.log_formatter = "%(levelname)s - %(asctime)s - %(message)s - %(funcName)s"

        self.log_level = self.log_level if self.log_level in [
            "CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "NOTSET"
        ] else None

        self._logger = logging.getLogger(self.logger_name)
        self._logger.setLevel(self.log_level)

        if self.log_type == "rich":
            self._base_handler = BaseRichHandler()
        elif self.log_type == "stream":
            self._base_handler = BaseStreamHandler()
            self._base_configuration_log_colored()
        else:
            self._base_handler = BaseRichHandler()

        self._logger.addHandler(
            ContextHandler(self._base_handler).
            get_handler(
                self.log_level,
                self.log_formatter
            )
        )

    def _base_configuration_log_colored(self) -> coloredlogs.install:
        coloredlogs.install(level=self.log_level,
                            logger=self.logger,
                            fmt=self.log_formatter,
                            milliseconds=True)

    @property
    def logger(self) -> Callable:
        return self._logger
