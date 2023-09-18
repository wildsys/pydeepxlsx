#!/usr/bin/env python
# coding: utf-8

from distutils.core import setup

setup(
    name='pydeepxlsx',
    version='1.0',
    description='Create an XLSX file based on a template, preserving formulas, using openpyxl',
    author='WildSys',
    author_email='hello@wildsys.io',
    url='https://www.python.org/sigs/distutils-sig/',
    packages=['pydeepxlsx'],
    install_requires=[
        'python-slugify',
        'openpyxl'
    ]
)
