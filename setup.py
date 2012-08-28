#!/usr/bin/env python

from setuptools import setup

try:
	import configparser
except ImportError:
	install_requires = ['configparser']
else:
	# python 3.2 doesn't need this module, and in fact will break
	install_requires = []

setup(
	name="configparser_plus",
	version="0.2",
	description="Library to provide a better version of ConfigParser in Python 2 and 3.",
	author="Michael Farrell",
	author_email="micolous@gmail.com",
	url="https://github.com/micolous/configparser_plus",
	install_requires=install_requires,
	py_modules=['configparser_plus'],
)

