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

import os

import header
import footer
from pyCI import VERSION
from routing import route_to


def generate_html():
    route = os.environ.get('PATH_INFO', '/')

    title, body = route_to(route)

    if title == 'mime::svg':
        print 'Content-Type: image/svg+xml; charset=UTF-8'
        print ''
        print body
        return

    print 'Content-Type: text/html; charset=UTF-8'
    print ''
    print '''<!DOCTYPE HTML>
<html>
  <head>
    <title>pyCI - {0}</title>
    <meta name="generator" content="pyCI v{1}"/>
    <meta name="robots" content="index, nofollow"/>
    <link rel="stylesheet" type="type/css" href="/pyci.css"/>
    <link rel="shortcut icon" href="/favicon.ico"/>
    <script src="/jquery.js"></script>
    <script src="/pyci.js"></script>
  </head>
  <body>
    {2}
    <div class="content">{3}</div>
    {4}
  </body>
</html>'''.format(title, VERSION, header.html(), body, footer.html())
