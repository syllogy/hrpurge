# -*- coding: utf-8 -*-

import sys
import logging
from typing import NoReturn, Text
from abc import ABCMeta, abstractmethod

from rich.logging import RichHandler
from pythonjsonlogger import jsonlogger


class StrategyHandler(metaclass=ABCMeta):

    @abstractmethod
    def handler(self,
                log_level: Text,
                log_formatter: Text) -> NoReturn: pass


class BaseRichHandler(StrategyHandler):

    @staticmethod
    def handler(log_level: Text,
                log_formatter: Text):
        rich_handler = RichHandler(rich_tracebacks=True)
        rich_handler.setLevel(log_level)
        rich_handler.setFormatter(jsonlogger.JsonFormatter(log_formatter))
        return rich_handler


class BaseStreamHandler(StrategyHandler):

    @staticmethod
    def handler(log_level: Text,
                log_formatter: Text) -> logging.StreamHandler:
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(log_level)
        stream_handler.setFormatter(jsonlogger.JsonFormatter(log_formatter))
        return stream_handler


class ContextHandler:
    def __init__(self,
                 strategy: StrategyHandler) -> NoReturn:
        self._strategy = strategy

    @property
    def strategy(self) -> StrategyHandler:
        return self._strategy

    def get_handler(self, log_level: Text, log_formatter: Text) -> NoReturn:
        return self._strategy.handler(log_level, log_formatter)
