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

from sites import index, invalid, project
from helper import badges


def route_to(route):
    route = route.split('/')

    if route[1] == '':
        return index.page()
    elif len(route) >= 4 and route[1] == 'project' and route[3] == 'badge.svg':
        return badges.image(route)
    elif route[1] == 'project':
        return project.page(route)

    return invalid.page()
