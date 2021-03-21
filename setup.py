# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from hrpurge import __version__

# ==============================================================================
# CONSTANTS
# ==============================================================================

NAME = "hrpurge"

LONG_DESCRIPTION = """
Python hrpurge is a CLI tool for automatically purge helm releases that is deploy into
your Kubernetes Cluster, based on labels that you can pass and filter your releases.
""".strip()

SHORT_DESCRIPTION = """
A CLI tool that help you delete old releases of a helm chart deployed in K8S.""".strip()

DEPENDENCIES = [
    "art",
    "colorama",
    "coloredlogs",
    "fire",
    "pyfiglet",
    "python-json-logger",
    "rich",
    "termcolor",
    "tqdm",
]

URL = "https://github.com/lpmatos/hrpurge"
EMAIL = "luccapsm@gmail.com"
AUTHOR = "Lucca Pessoa da Silva Matos"
REQUIRES_PYTHON = ">=3.6.0"
VERSION = __version__


# ==============================================================================
# BUILD PACKAGE
# ==============================================================================

setup(
    name=NAME,
    author=AUTHOR,
    author_email=EMAIL,
    version=VERSION,
    license="MIT license",
    url=URL,
    packages=find_packages(include=[NAME], exclude=[
                           "tests", "*.tests", "*.tests.*", "tests.*"]),
    package_data={NAME: ["py.typed"]},
    zip_safe=False,
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    install_requires=DEPENDENCIES,
    python_requires=REQUIRES_PYTHON,
    entry_points=f"""
        [console_scripts]
        {NAME}={NAME}.main:main
    """,
    keywords=[
        "cli",
        "helm",
        "python"
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Helm",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    project_urls={
        "Repository": "https://github.com/lpmatos/hrpurge",
    },
)
