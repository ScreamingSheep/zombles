#!/usr/bin/python
# -*- coding: utf-8 -*-
from setuptools import setup

version = '1.0.0'

setup(
    name='zombles',
    version=version,
    author='Rishi Ramraj',
    author_email='source@bestpremise.com',
    url='http://www.bestpremise.com',
    license=license,
    packages=[
        'zombles',
    ],
    install_requires=[
        'setuptools',
        'PyMySQL3',
        'webob',
    ],
    entry_points={
        'console_scripts': [
            'zombles.server = zombles.server:main',
            'zombles.client = zombles.client:main',
        ],
    },
)
