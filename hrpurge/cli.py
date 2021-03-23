# -*- coding: utf-8 -*-

import sys
from time import sleep
from typing import Dict, NoReturn

from bullet import Bullet, Check, Input, Numbers, VerticalPrompt, YesNo, colors
from rich.console import Console
from rich.markdown import Markdown

from hrpurge.cli_version import show_version
from hrpurge.const import MARKDOWN_WELCOME
from hrpurge.setup import ANIMATION, CONFIG


def cli(information: Dict) -> NoReturn:
    console = Console()
    markdown = Markdown(MARKDOWN_WELCOME)
    console.print(markdown)
    print()

    if information["--version"]:
        show_version()
        sys.exit(1)

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
                    "Who are you? ",
                    default="Batman",
                    word_color=colors.foreground["yellow"],
                ),
                Input("Really? ", word_color=colors.foreground["yellow"]),
                Numbers(
                    "How old are you? ",
                    word_color=colors.foreground["yellow"],
                    type=int,
                ),
                Bullet(
                    "What is your favorite programming language? ",
                    choices=["C++", "Python", "Javascript", "Not here!"],
                    bullet=" >",
                    margin=2,
                    bullet_color=colors.bright(colors.foreground["cyan"]),
                    background_color=colors.background["black"],
                    background_on_switch=colors.background["black"],
                    word_color=colors.foreground["white"],
                    word_on_switch=colors.foreground["white"],
                ),
                Check(
                    "What food do you like? ",
                    choices=[
                        "🍣   Sushi",
                        "🍜   Ramen",
                        "🌭   Hotdogs",
                        "🍔   Hamburgers",
                        "🍕   Pizza",
                        "🍝   Spaghetti",
                        "🍰   Cakes",
                        "🍩   Donuts",
                    ],
                    check=" √",
                    margin=2,
                    check_color=colors.bright(colors.foreground["red"]),
                    check_on_switch=colors.bright(colors.foreground["red"]),
                    background_color=colors.background["black"],
                    background_on_switch=colors.background["white"],
                    word_color=colors.foreground["white"],
                    word_on_switch=colors.foreground["black"],
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

    console = Console()
    tasks = [f"task {n}" for n in range(1, 11)]
    with console.status("[bold green]Working on tasks...") as _:
        while tasks:
            task = tasks.pop(0)
            sleep(1)
            console.log(f"{task} complete")
        print()

    if CONFIG.get_env("CI"):
        print("Done! Finish!")
    else:
        ANIMATION.finish()
