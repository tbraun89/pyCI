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

from pyCI.util import tokenize_config


class TestTokenizeConfig(unittest.TestCase):
    def runTest(self):
        tokens = tokenize_config('data/tokenize_config_0.txt')

        self.assertItemsEqual(tokens, [
            'command',
            'property',
            'value0',
            'category.property',
            'value1',
            'property',
            'value1',
            'new_command',
            'value_string',
            'This is a String',
            'property_after_many_lines',
            'value2'
        ])


def suite():
    my_suite = unittest.TestSuite()
    my_suite.addTest(TestTokenizeConfig())
    return my_suite
