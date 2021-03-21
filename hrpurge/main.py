# -*- coding: utf-8 -*-
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
  --kubeconfig=<kubeconfig>     path to the kubeconfig file
  --kubecontext=<kubecontext>    name of the kubeconfig context to use

Environment variables:

| Name             | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| $KUBECONFIG      | set an alternative Kubernetes configuration file (default "~/.kube/config") |
"""

from docopt import docopt
from hrpurge.cli import cli
from hrpurge import __version__


def main():
    arguments = dict(docopt(__doc__))
    cli(arguments)
