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
import tempfile
import os

from pyCI.util import DB


class TestDB(unittest.TestCase):
    def setUp(self):
        self.db_file = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.db_file[1])

    def runTest(self):
        db = DB(self.db_file[1])

        self.assertEquals(len(db.project_list()), 0)

        db.add_project('Project 1', 'c0cd61a', 0)
        self.assertEquals(len(db.project_list()), 1)
        self.assertEquals(db.current_git_id('Project 1'), 'c0cd61a')
        self.assertEquals(db.project_slug_by_name('Project 1'), 'project-1')
        self.assertEquals(db.project_status_by_slug('project-1'), 0)
        self.assertEquals(len(db.project_log_list('Project 1')), 0)

        db.add_log('Project 1', 'Demo Log\nLine 2')
        self.assertEquals(len(db.project_log_list('Project 1')), 1)
        self.assertEquals(db.project_log_list('Project 1')[0][0], 'Demo Log\nLine 2')

        db.update_status('Project 1', 1)
        db.update_git_id('Project 1', '8c489ff')
        self.assertEquals(len(db.project_list()), 1)
        self.assertEquals(db.project_list()[0][1], '8c489ff')
        self.assertEquals(db.project_list()[0][2], 1)

        db.add_project('Project 2', 'fb326d5', 0)
        self.assertEquals(len(db.project_list()), 2)

        db.add_project('Project 1', 'c0cd61a', 0)
        self.assertEquals(len(db.project_list()), 2)


def suite():
    my_suite = unittest.TestSuite()
    my_suite.addTest(TestDB())
    return my_suite