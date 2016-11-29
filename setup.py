#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of mtgsdk.
# https://github.com/MagicTheGathering/mtg-sdk-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Andrew Backes <backes.andrew@gmail.com>

import os
import sys

from setuptools import setup, find_packages

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'mtgsdk'))
from mtgsdk.config import __version__, __pypi_packagename__, __github_username__, __github_reponame__

tests_require = [
    'hypothesis'
]

url = 'https://github.com/' + __github_username__ + '/' + __github_reponame__
download_url = "{}/tarball/{}".format(url, __version__)

print(find_packages())

setup(
    name=__pypi_packagename__,
    version=__version__,
    packages=['mtgsdk'],
    install_requires=['attrs>=16.2.0', 'requests>=2.12.0', 'toolz>=0.8.0']
)
