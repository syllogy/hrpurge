# -*- coding: utf-8 -*-

from typing import NoReturn

from asciimatics.scene import Scene
from asciimatics.screen import ManagedScreen
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText


class Animation():

    @staticmethod
    def finish() -> NoReturn:
        with ManagedScreen() as screen:
            effects = [
                Cycle(
                    screen,
                    FigletText("DONE!", font='big'),
                    int(screen.height / 2 - 8)),
                Cycle(
                    screen,
                    FigletText("EXECUTION FINISHED!", font='big'),
                    int(screen.height / 2 + 3)),
                Stars(screen, 200)
            ]
            screen.play([Scene(effects, duration=100)], repeat=False)
