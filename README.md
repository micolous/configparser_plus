# ConfigParserPlus #

An extension library to Python's `SafeConfigParser` to provide defaults as a two dimensional dict, making it a little bit easier to use.

Copyright 2011-2012 Michael Farrell.  Licensed under the GNU LGPLv3.

Version 0.2-dev

## Note: This library is deprecated. ##

I'm retiring this library.  ConfigParser from Python 3.2 implements the key feature of this library through the `read_dict` method, and there is also a backport of this library available for Python 2.6.

I've ported this library to use that library instead now, and this will be retired.

Unfortunately I got half way through writing up some unit tests and implementing support for Python 3.2 when discovering this.  So there are some new tests to work out a couple of bugs in the previous version of the library.

It will probably introduce some API differences, it is based around the Python 3.2 version of the ConfigParser.

The software that uses this library is mostly my own, so I will be porting my own software away from using this library in the future.  You shouldn't write any new software that uses this library.


## Requirements ##

* Python 2.6 or later, or Python 3.2 or later.

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

* Note: As of version 0.2, this will use the configparser3 behaviour, where this is no longer the case -- it will return True even if the value comes from the default configuration.


