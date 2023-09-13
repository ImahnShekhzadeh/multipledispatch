#!/usr/bin/env python

from os.path import exists

from setuptools import setup

setup(
    name="multipledispatch",
    version="1.0.2",
    description="Multiple dispatch",
    url="https://github.com/ImahnShekhzadeh/multipledispatch",
    author="Imahn Shekhzadeh",
    author_email="imahn.shekhzadeh@hesge.ch",
    license="BSD",
    keywords="dispatch",
    packages=["multipledispatch"],
    long_description=(open("README.rst").read() if exists("README.rst") else ""),
    zip_safe=False,
)
