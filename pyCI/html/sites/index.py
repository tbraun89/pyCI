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

import urllib

from pyCI.util.db import DB
from pyCI.repository import Repository


def page():
    title = 'Project Browser'
    icon = ''
    color = ''

    db = DB('/etc/pyci.db')
    table_rows = ''

    for project in db.project_list():
        if project[2] == Repository.UNKNOWN or project[2] == Repository.VCS_ERROR:
            icon = '<i class="icon-help"></i>'
            color = 'yellow'
        elif project[2] == Repository.FAILED:
            icon = '<i class="icon-emo-cry"></i>'
            color = 'red'
        elif project[2] == Repository.SUCCESS:
            icon = '<i class="icon-emo-happy"></i>'
            color = 'green'

        table_rows += '''
<tr class="{0}">
  <td><a href="project/{5}">{1}</a></td>
  <td><a href="project/{5}">{2}</a></td>
  <td><a href="project/{5}">{3}</a></td>
  <td><a href="project/{5}">{4}</a></td>
</tr>
'''.format(color, icon, project[0], project[1], project[3], urllib.pathname2url(project[0]))

    body = '''
<table class="list nowrap">
  <thead>
    <tr>
      <th>Status</th>
      <th>Name</th>
      <th>Commit</th>
      <th>Last Change</th>
    </tr>
  </thead>
  <tbody>
    {0}
  </tbody>
</table>
'''.format(table_rows)

    return title, body