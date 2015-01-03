# pyCI
# Copyright (C) 2014  Torsten Braun
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import unittest
import logging
from StringIO import StringIO


class TestGetLogger(unittest.TestCase):
    def setUp(self):
        from pyCI.util import get_logger
        self.logger = get_logger('TestGetLogger')

    def runTest(self):
        self.assertIsInstance(self.logger, logging.Logger)
        self.assertIsInstance(self.logger.handlers[0], logging.StreamHandler)


class TestLogging(unittest.TestCase):
    def setUp(self):
        from pyCI.util import get_logger
        self.logger = get_logger('TestLogging')
        self.stream = StringIO()
        self.handler = logging.StreamHandler(self.stream)

        for handler in self.logger.handlers:
            self.logger.removeHandler(handler)

        self.logger.addHandler(self.handler)

    def runTest(self):
        self.logger.debug('Debug Message')
        self.logger.info('Info Message')
        self.logger.warning('Warning Message')
        self.logger.error('Error Message')
        self.logger.critical('Critical Message')
        self.handler.flush()

        self.assertEquals(self.stream.getvalue(), 'Info Message\nWarning Message\nError Message\nCritical Message\n')


def suite():
    my_suite = unittest.TestSuite()
    my_suite.addTest(TestGetLogger())
    my_suite.addTest(TestLogging())
    return my_suite
