# -*- coding: utf-8 -*-

import sys
from time import sleep
from typing import NoReturn, Dict

from rich.console import Console
from rich.markdown import Markdown

from hrpurge.log import Log
from hrpurge.settings import Config
from hrpurge.constants import WELCOME
from hrpurge.animation import Animation
from hrpurge.cli_version import show_version

animation = Animation()
log = Log("INFO", "rich", "logger").logger
config = Config()


def header() -> NoReturn:
    console = Console()
    markdown = Markdown(WELCOME)
    console.print(markdown)
    print()


def cli(information: Dict) -> NoReturn:
    header()

    if information["--version"]:
        show_version()
        sys.exit(1)

    console = Console()
    tasks = [f"task {n}" for n in range(1, 11)]
    with console.status("[bold green]Working on tasks...") as _:
        while tasks:
            task = tasks.pop(0)
            sleep(1)
            console.log(f"{task} complete")
        print()

    if config.get_env("CI"):
        print("Done! Finish!")
    else:
        animation.finish()
