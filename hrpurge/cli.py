# -*- coding: utf-8 -*-

import sys
from time import sleep
from typing import Dict, NoReturn

from bullet import Input, Numbers, VerticalPrompt, YesNo, colors
from rich.console import Console
from rich.markdown import Markdown

from hrpurge.cli_version import show_version
from hrpurge.const import MARKDOWN_WELCOME
from hrpurge.log import Log
from hrpurge.setup import ANIMATION, CONFIG


def cli(information: Dict) -> NoReturn:
    console = Console()
    markdown = Markdown(MARKDOWN_WELCOME)
    console.print(markdown)
    print()
    enabel_ci = False

    if information["-v"] or information["--version"]:
        show_version()
        sys.exit(1)

    if information["--ci"]:
        enabel_ci = True

    if information["--quiet"]:
        log = Log("CRITICAL", "rich", "logger").logger
    else:
        log = Log("INFO", "rich", "logger").logger

    if information["--interactive"]:
        console = Console()
        markdown = Markdown("# Interactive")
        console.print(markdown)
        print()

        promt = VerticalPrompt(
            [
                YesNo(
                    "Are you a student? ",
                    word_color=colors.foreground["yellow"],
                ),
                YesNo(
                    "Are you a good student? ",
                    default="y",
                    word_color=colors.foreground["yellow"],
                ),
                Input(
                    "Path of your kubeconfig",
                    default="~",
                    word_color=colors.foreground["yellow"],
                ),
                Input("Really? ", word_color=colors.foreground["yellow"]),
                Numbers(
                    "How old are you? ",
                    word_color=colors.foreground["yellow"],
                    type=int,
                ),
            ]
        )
        print("\n")
        result = promt.launch()
        promt.summarize()
        print(result)
        print()

    console = Console()
    markdown = Markdown("# Work")
    console.print(markdown)
    print()

    log.info("Validando")

    console = Console()
    tasks = [f"task {n}" for n in range(1, 11)]
    with console.status("[bold green]Working on tasks...") as _:
        while tasks:
            task = tasks.pop(0)
            sleep(1)
            console.log(f"{task} complete")
        print()

    console = Console()
    markdown = Markdown("# Results")
    console.print(markdown)
    print()

    if enabel_ci or CONFIG.get_env("CI"):
        print("Done! Finish!")
    else:
        ANIMATION.finish()
