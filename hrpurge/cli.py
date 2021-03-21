# -*- coding: utf-8 -*-

import sys
from time import sleep

from rich.console import Console
from rich.markdown import Markdown

from hrpurge.constants import WELCOME
from hrpurge.animation import Animation
from hrpurge.log import Log
from hrpurge.cli_version import show_version

animation = Animation()
log = Log("INFO", "rich", "logger").logger


def header():
    console = Console()
    markdown = Markdown(WELCOME)
    console.print(markdown)
    print()


def cli(information):
    header()

    if information["--version"]:
        show_version()
        sys.exit(1)

    sleep(5)
    animation.finish()
