"""
Description: A Python module to use easily the osu!api V1.
Author: LostPy
License: MIT
Date: 2021-01-11
"""

from setuptools import setup, find_packages

import osu

__doc__ = """a small module for easy use of the api."""


setup(
	name='osu-api.py',
	version='1.0',
	author='LostPy',
	description="A small module for easy use of the osu!api",
	long_description=__doc__,
    package_dir = {'osu': './osu'},
    package_data = {'': ['LICENSE.txt']},
	include_package_data=True,
	url='https://github.com/LostPy/OsuData',
	classifiers=[
        "Programming Language :: Python",
        "Development Status :: Functionnal - improvement in progress",
        "License :: MIT",
        "Natural Language :: French",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5+",
        "Topic :: osu!",
    ],
    license='MIT',
    packages = find_packages()
    )
