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

from pyCI.html.helper import badges


class TestUnknownBadge(unittest.TestCase):
    def runTest(self):
        result = badges.badge(badges.UNKNOWN)

        self.failUnless('build' in result)
        self.failUnless('unknown' in result)
        self.failUnless('#dfb317' in result)


class TestPassingBadge(unittest.TestCase):
    def runTest(self):
        result = badges.badge(badges.PASSING)

        self.failUnless('build' in result)
        self.failUnless('passing' in result)
        self.failUnless('#4c1' in result)


class TestFailingBadge(unittest.TestCase):
    def runTest(self):
        result = badges.badge(badges.FAILING)

        self.failUnless('build' in result)
        self.failUnless('failing' in result)
        self.failUnless('#e05d44' in result)


def suite():
    my_suite = unittest.TestSuite()
    my_suite.addTest(TestUnknownBadge())
    my_suite.addTest(TestPassingBadge())
    my_suite.addTest(TestFailingBadge())
    return my_suite