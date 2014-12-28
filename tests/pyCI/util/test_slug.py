# -*- coding: utf-8 -*-

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

from pyCI.util import slug


class TestSlugify(unittest.TestCase):
    def runTest(self):
        self.assertEquals(slug.slugify('This is a Test'), 'this-is-a-test')
        self.assertEquals(slug.slugify('1 2 34'), '1-2-34')
        self.assertEquals(slug.slugify('Project (master branch)'), 'project-master-branch')
        self.assertEquals(slug.slugify('!"$%&/()=?A!"$%&/()=?`B*+~\'#<>|,;.:-_C'), 'ab-_c')
        self.assertEquals(slug.slugify(u'German ÜÄÖöäü Project [master]'), 'german-uaooau-project-master')


def suite():
    my_suite = unittest.TestSuite()
    my_suite.addTest(TestSlugify())
    return my_suite
