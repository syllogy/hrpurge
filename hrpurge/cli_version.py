# -*- coding: utf-8 -*-

from typing import NoReturn

import arrow
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown

from . import __version__


def show_version() -> NoReturn:
    console = Console()

    markdown = Markdown("# Version")
    console.print(markdown)
    print()

    table = Table(show_header=True, header_style="bold blue")
    table.add_column("NAME", style="dim", width=12,
                     footer_style="bright_green")
    table.add_column(
        "CLI VERSION", style="dim", width=12, footer_style="bright_green"
    )
    table.add_column(
        "SYSTEM DATE", style="dim", width=20, footer_style="bright_green"
    )
    table.add_row(
        "🤖 hrpurge",
        __version__,
        str(arrow.utcnow().to("America/Sao_Paulo").format("YYYY-MM-DD HH:mm:ss")),
    )
    console.print(table)
