#!/usr/bin/env python

from configparser_plus import *
from os.path import dirname, join

DEFAULTS = {
	'test1': {
		'hello': 'no',
		'some_integer': '16',
		'some_string': 'bob',
	}
}

TEST_PATH = dirname(__file__)
print TEST_PATH

def test1_0():
	"Make sure defaults are set correctly."
	config = ConfigParserPlus(DEFAULTS)
	
	for k, v in DEFAULTS['test1'].iteritems():
		assert config.get('test1', k) == v
	
	# check it again, but cast things now.
	assert config.getboolean('test1', 'hello') == False
	assert config.getint('test1', 'some_integer') == 16
	
	# ensure that if allow_no_value=False, throws an exception
	try:
		config.get('test1', 'unknown_item')
	except NoOptionError:
		assert True
	else:
		assert False, '.get did not throw NoOptionError for unknown item'
		
	# repeat the test for unknown sections
	try:
		config.get('unknown_section', 'unknown_item')
	except NoSectionError:
		assert True
	else:
		assert False, '.get did not throw NoSectionError for unknown item'

def test1_1():
	"Read from test1-1.ini"
	config = ConfigParserPlus(DEFAULTS)
	path = join(TEST_PATH, 'test1-1.ini')
	
	assert config.read(path), 'Failure reading from %r' % path
	assert config.getboolean('test1', 'hello') == True
	assert config.getint('test1', 'some_integer') == 42
