#!/usr/bin/env python
"""
Library to give extra features to SafeConfigParser.
Copyright 2011-2012 Michael Farrell <http://micolous.id.au/>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from configparser import ConfigParser, NoOptionError, NoSectionError, InterpolationMissingOptionError

__all__ = [
	'ConfigParserPlus',
	'NoOptionError',
	'NoSectionError',
	'InterpolationMissingOptionError',
]
	
class ConfigParserPlus(ConfigParser):
	"""
ConfigParserPlus changes the behaviour of the SafeConfigParser constructor so it takes in a two-dimensional dict of defaults (which is much simpler to handle).  You could also pass it something that implements a 2D dict.

has_option performs identically to the underlying SafeConfigParser -- if an option is not in the configuration, it will return False (even if a default is available).

Default values will be cast for getint and getfloat, unless the default value is None.  get and getfloat will not cast values.
	"""

	def __init__(self, defaults, allow_no_value=False):
		super(ConfigParserPlus, self).__init__()
		
		# pass the defaults back through to read_dict
		self.read_dict(defaults)
		
		# apparently self._defaults is used by the default implementation.
		self._cfp_defaults = defaults
		self._allow_no_value = allow_no_value
		
	def get(self, *args, **kwargs):
		"Emulate the 'allow_no_value' behaviour"
		
		if self._allow_no_value:
			try:
				return super(ConfigParserPlus, self).get(*args, **kwargs)
			except (NoOptionError, NoSectionError) as _:
				return None
		else:
			return super(ConfigParserPlus, self).get(*args, **kwargs)

	def defaults(self):
		"Return the 2D dict that is providing defaults.."
		return self._cfp_defaults
