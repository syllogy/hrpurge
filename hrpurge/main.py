# -*- coding: utf-8 -*-
# flake8: noqa: E501
"""
Description: A CLI tool that help you delete old releases of a helm chart deployed in K8S.

Usage:
  hrpurge [options]
  hrpurge -h | --help
  hrpurge -v | --version

Options:
  -h --help                         show this help message and exit
  -q --quiet                        report only errors
  -i --interactive                  enable interactive mode
  -d DAYS --days=DAYS               date filter to delete helm releases [default: 15]

  --helm-release-filter=RELEASE     helm release regex filter - if this value is
                                    equal to "all", filter all helm releases [default: ^feature-.+]
  --namespace-filter=NAMESPACE      namespace regex filter - if this value is
                                    equal to "all", filter all namespaces [default: ^project-.+]

  --kubeconfig=KUBECONFIG           path to the kubeconfig file [default: ~/.kube/config]
  --kubecontext=KUBECONTEXT         name of the kubeconfig context to use
  --ci                              enable to CI context
  --dry-run                         enable dry run mode, nothing will be deleted
  --version                         show version and exit

Environment variables:

| Name                 | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| $OLDER_THAN          | date filter to delete helm releases                                         |
| $HELM_RELEASE_FILTER | helm release regex filter - if equal to "all", filter all helm releases     |
| $NAMESPACE_FILTER    | namespace regex filter - if equal to "all", filter all namespaces           |
| $KUBECONTEXT         | sets a context entry in kubeconfig                                          |
| $KUBECONFIG          | set an alternative Kubernetes configuration file (default "~/.kube/config") |
"""

from typing import NoReturn

from docopt import docopt

from hrpurge.cli import cli


def main() -> NoReturn:
    arguments = dict(docopt(__doc__))
    cli(arguments)
