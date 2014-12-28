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

import sqlite3
from datetime import datetime


class DB:
    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file)

        with self.connection:
            cur = self.connection.cursor()
            cur.execute('''
CREATE TABLE IF NOT EXISTS project_infos(name TEXT PRIMARY KEY, git_id TEXT, status INT, date TEXT)
''')
            cur.execute('''
CREATE TABLE IF NOT EXISTS project_logs(log TEXT, project_name TEXT, date TEXT)
''')
            self.connection.commit()

    def add_project(self, name, git_id, status):
        with self.connection:
            cur = self.connection.cursor()
            cur.execute('SELECT * FROM project_infos WHERE name="{0}"'.format(name))
            self.connection.commit()

            if len(cur.fetchall()) == 0:
                cur.execute('''
INSERT OR IGNORE INTO project_infos (name, git_id, status, date, slug) VALUES("{0}", "{1}", {2}, "{3}", "{4}")
'''.format(name, git_id, status, datetime.now().strftime("%Y-%m-%d %H:%M"), slugify(name)))
                self.connection.commit()

    def add_log(self, name, message):
        with self.connection:
            cur = self.connection.cursor()
            cur.execute('''
INSERT INTO project_logs (log, project_name, date) VALUES("{0}", "{1}", "{2}")
'''.format(message, name, datetime.now().strftime("%Y-%m-%d %H:%M")))
            self.connection.commit()

    def update_status(self, name, status):
        with self.connection:
            cur = self.connection.cursor()
            cur.execute('''
UPDATE project_infos SET status={0}, date="{2}" WHERE name="{1}"
'''.format(status, name, datetime.now().strftime("%Y-%m-%d %H:%M")))
            self.connection.commit()

    def update_git_id(self, name, git_id):
        with self.connection:
            cur = self.connection.cursor()
            cur.execute('UPDATE project_infos SET git_id="{0}" WHERE name="{1}"'.format(git_id, name))
            self.connection.commit()

    def current_git_id(self, name):
        with self.connection:
            cur = self.connection.cursor()
            cur.execute('SELECT git_id FROM project_infos WHERE name="{0}"'.format(name))
            self.connection.commit()

            return cur.fetchone()[0]

    def project_list(self):
        with self.connection:
            cur = self.connection.cursor()
            cur.execute('SELECT * FROM project_infos')
            self.connection.commit()

            return cur.fetchall()

    def project_log_list(self, name):
        with self.connection:
            cur = self.connection.cursor()
            cur.execute('SELECT * FROM project_logs WHERE project_name="{0}"'.format(name))
            self.connection.commit()

            return cur.fetchall()
