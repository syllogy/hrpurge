# -*- coding: utf-8 -*-
# flake8: noqa: E501
"""
Description: A CLI tool that help you delete old releases of a helm chart deployed in K8S.

Usage:
  hrpurge [options]
  hrpurge -h | --help
  hrpurge --version

Options:
  -h --help                     show this help message and exit
  --version                     show version and exit
  -q --quiet                    report only errors
  -i --interactive              enable interactive mode
  --kubeconfig=<kubeconfig>     path to the kubeconfig file [default: ~/.kube/config]
  --kubecontext=<kubecontext>   name of the kubeconfig context to use

Environment variables:

| Name             | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| $KUBECONTEXT     | sets a context entry in kubeconfig                                          |
| $KUBECONFIG      | set an alternative Kubernetes configuration file (default "~/.kube/config") |
"""

from typing import NoReturn

from docopt import docopt

from hrpurge.cli import cli


def main() -> NoReturn:
    arguments = dict(docopt(__doc__))
    cli(arguments)
