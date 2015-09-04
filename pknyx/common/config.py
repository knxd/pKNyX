# -*- coding: utf-8 -*-

""" Python KNX framework.

License
=======

 - B{pKNyX} (U{http://www.pknyx.org}) is Copyright:
  - (C) 2013-2015 Frédéric Mantegazza

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
or see:

 - U{http://www.gnu.org/licenses/gpl.html}

Module purpose
==============

Global configuration

@author: Frédéric Mantegazza
@copyright: (C) 2013-2015 Frédéric Mantegazza
@license: GPL
"""

__revision__ = "$Id$"

import sys
import os.path


# Name
APP_NAME = "pKNyX"
APP_VERSION = "0.9.post3"

# Paths
HOME_DIR = os.path.expanduser("~")
if sys.platform == 'win32':
    DATA_STORAGE_DIR = HOME_DIR  # Find a way to retreive the "My Documents" dir in all languages
    TMP_DIR = os.path.expandvars("$TEMP")
else:
    DATA_STORAGE_DIR = HOME_DIR
    TMP_DIR = "/tmp"

# Logger
LOGGER_STREAM_FORMAT = "%(threadName)s::%(message)s"
LOGGER_LEVEL = "debug"
