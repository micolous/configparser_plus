# ConfigParserPlus #

An extension library to Python's `SafeConfigParser` to provide defaults as a two dimensional dict, making it a little bit easier to use.

Copyright 2011-2012 Michael Farrell.  Licensed under the GNU LGPLv3.

## Requirements ##

* Python 2.3 or later, or Python 3.0 or later.

## Usage ##

There is some documentation in Python's `Raw/SafeConfigParser` which indicates about dict types, however this is purely for pulling options out.  The change in `ConfigParserPlus` is it allows you to specify a two-dimensional dict of default values.

`ConfigParserPlus` is a subclass of `SafeConfigParser`.

Otherwise, the library is the same.   For example:

    #!/usr/bin/env python
	from configparser_plus import ConfigParserPlus
	
	# Create some default values for our file.
	config = ConfigParserPlus(defaults={
	  'Mail': {
	    'MAPI': 1,
	  },
	  'MCI Extensions.BAK': {
	    '3g2': 'MPEGVideo',
		'3gp': 'MPEGVideo'
	  }
	})
	
	config.readfp(open('/c/Windows/win.ini', 'rb'))

You can then access keys as normal with the `get*` functions.

If the key is not set in a loaded configuration, but is in the default, then the `get*` function will return the default value, however `has_option` will return `False`.


