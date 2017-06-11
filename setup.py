#!/usr/bin/env python
# -*- Coding : UTF-8 -*-

_author = "Eduardo S. Pereira"
_date = "11/06/2017"
_contact = "pereira.somoza@gmail.com"


import os
import glob
from setuptools import setup



def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="rgbfits",
    version="1.0",
    author="Eduardo dos Santos Pereira",
    author_email="pereira.somoza@gmail.com",
    description=("Tool for Convert latex to doc and html"),
    license="GNU v3",
    keywords="fits, png, rgb",
    url="https://github.com/duducosmos/rgbfits",
    install_requires=['easygui', 'astropy', 'numpy', 'scipy', 'pillow'],
    py_modules = ['rgbfits', 'trilogy', 'im2rgbfits'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: GNU V3",
    ],
    entry_points = {"console_scripts":
                    ["rgbfits = rgbfits:main", ]},
)
