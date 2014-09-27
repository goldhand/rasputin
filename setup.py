# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import rasputin
version = rasputin.__version__

setup(
    name='rasputin',
    version=version,
    author='',
    author_email='dekanbro@gmail.com',
    packages=[
        'rasputin',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.5',
    ],
    zip_safe=False,
    scripts=['rasputin/manage.py'],
)