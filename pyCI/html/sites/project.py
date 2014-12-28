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

import hashlib
import os

from pyCI.util.db import DB


def page(route):
    title = route[2]
    db = DB('/etc/pyci.db')
    body = ''

    slug = db.project_slug_by_name(route[2])
    host = os.environ.get('HTTP_REFERER', 'http://{0}/'.format(os.environ.get('HTTP_HOST', '')))

    badge_info = '''
<div class="info-section">
  <img src="/project/{0}/badge.svg" /><br />
  <div class="section">
    <lable>Badge URL:</lable>
    <input type="text" value="{1}project/{0}/badge.svg" />
  </div>
</div>
<hr />
'''.format(slug, host)

    try:
        for log in db.project_log_list(route[2]):
            body += '<h3 id="{2}">{0} - {1}</h3>'.format(log[2], log[1], hashlib.sha1(log[2]).hexdigest())
            body += '<table id="code_{0}" class="code hidden">'.format(hashlib.sha1(log[2]).hexdigest())
            current_log = log[0].split('\n')
            del current_log[-1]

            for i, line in enumerate(current_log):
                body += '<tr><td class="num">{0}:</td><td class="out">{1}</td></tr>'.format(i, line)

            body += '</table>'
    except:
        body = '''
<div class="error">
  The project {0} has no logs.
</div>
'''.format(route[2])

    body = badge_info + body

    return title, body