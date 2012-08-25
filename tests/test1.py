#!/usr/bin/env python

from configparser_plus import *
from os.path import dirname, join

DEFAULTS = {
	'test1': {
		'hello': 'no',
		'some_integer': '16',
		'some_string': 'bob',
		'interpolate': 'lol %(desu)s foo',
	}
}

TEST_PATH = dirname(__file__)

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

def test1_interpolate():
	"Test interpolation behaviour"
	config = ConfigParserPlus(DEFAULTS)
	
	# check that we default to not interpolating
	assert config.get('test1', 'interpolate') == DEFAULTS['test1']['interpolate']
	
	# check that missing interpolations fail
	try:
		config.get('test1', 'interpolate', raw=False)
	except InterpolationMissingOptionError:
		assert True
	else:
		assert False, '.get did not throw InterpolationMissingOptionError when interpolations are missing.'
	
	
	assert config.get('test1', 'interpolate', raw=False, vars={'desu': 'lagg'}) == 'lol lagg foo'
	
		
def test1_1():
	"Read from test1-1.ini"
	config = ConfigParserPlus(DEFAULTS)
	path = join(TEST_PATH, 'test1-1.ini')
	
	assert config.read(path), 'Failure reading from %r' % path
	assert config.getboolean('test1', 'hello') == True
	assert config.getint('test1', 'some_integer') == 42
	assert config.get('test1', 'interpolate') == 'hello %(desu)s sir'
	
	# check that interpolate works
	assert config.get('test1', 'interpolate', raw=False, vars={'desu': 'fine'}) == 'hello fine sir'
