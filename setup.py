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

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'mtgsdki'))
from mtgsdki.config import __version__, __pypi_packagename__, __github_username__, __github_reponame__

tests_require = [
    'hypothesis'
]

url = 'https://github.com/' + __github_username__ + '/' + __github_reponame__
download_url = "{}/tarball/{}".format(url, __version__)

setup(
    name=__pypi_packagename__,
    version=__version__,
    description='Magic: The Gathering SDK for magicthegathering.io',
    long_description='''
Magic: The Gathering SDK is a python wrapper around the MTG API located at magicthegathering.io
''',
    keywords='mtg sdk magic gathering gatherer api rest',
    author='Jonas Bulik',
    author_email='mrlordalfred@gmail.com',
    url=url,
    download_url=download_url,
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    # include_package_data=False,
    install_requires=[
        'requests>=2.12.0',
        'attrs>=16.2.0',
        'toolz>=0.8.0'
    ],
    extras_require={
        'tests': tests_require,
    },
)
