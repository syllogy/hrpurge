# -*- coding: utf-8 -*-

import semantic_version

version = semantic_version.Version("1.0.0")

__version__ = f"{version.major}.{version.minor}.{version.patch}"
