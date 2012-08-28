#!/usr/bin/env python

from distutils.core import setup

setup(
	name="configparser_plus",
	version="1.1",
	description="Library to provide a better version of ConfigParser in Python 2 and 3.",
	author="Michael Farrell",
	author_email="micolous@gmail.com",
	url="https://github.com/micolous/configparser_plus",
	requires=[
		'configparser',
	],
	py_modules=['configparser_plus'],
)

