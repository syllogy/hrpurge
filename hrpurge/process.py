# -*- coding: utf-8 -*-

import subprocess
import sys
from typing import Text, Tuple


class Process:
    @staticmethod
    def run_command(cmd: Text) -> Tuple[Text, Text]:
        try:
            process = subprocess.Popen(
                cmd,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                shell=True,
                universal_newlines=True,
            )
            output, errors = process.communicate()
            if process.returncode != 0:
                sys.stderr.write(
                    f"Run command failed - returncode - {process.returncode}"
                )
                sys.exit(1)
            return (output, errors)
        except subprocess.CalledProcessError as error:
            sys.stderr.write(
                f"Subprocess error when run the command {cmd} - {error}"
            )
            sys.exit(1)
