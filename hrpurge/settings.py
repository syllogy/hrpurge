# -*- coding: utf-8 -*-

from os import environ
from typing import Text, Type


class Config:

    @staticmethod
    def get_env(
        env: Type[Text],
        default: Type[Text] = None
    ) -> Text:
        return environ.get(env, default)
