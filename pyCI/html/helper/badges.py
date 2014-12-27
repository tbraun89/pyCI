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

# Images generated with http://shields.io/


FAILING = 1
PASSING = 2
UNKNOWN = 3


def badge(status):
    if status == FAILING:
        return '<svg xmlns="http://www.w3.org/2000/svg" width="81" height="18"><linearGradient id="a" x2="0" y2="100%"><stop offset="0" stop-color="#fff" stop-opacity=".7"/><stop offset=".1" stop-color="#aaa" stop-opacity=".1"/><stop offset=".9" stop-opacity=".3"/><stop offset="1" stop-opacity=".5"/></linearGradient><rect rx="4" width="81" height="18" fill="#555"/><rect rx="4" x="37" width="44" height="18" fill="#e05d44"/><path fill="#e05d44" d="M37 0h4v18h-4z"/><rect rx="4" width="81" height="18" fill="url(#a)"/><g fill="#fff" text-anchor="middle" font-family="DejaVu Sans,Verdana,Geneva,sans-serif" font-size="11"><text x="19.5" y="14" fill="#010101" fill-opacity=".3">build</text><text x="19.5" y="13">build</text><text x="58" y="14" fill="#010101" fill-opacity=".3">failing</text><text x="58" y="13">failing</text></g></svg>'
    elif status == PASSING:
        return '<svg xmlns="http://www.w3.org/2000/svg" width="90" height="18"><linearGradient id="a" x2="0" y2="100%"><stop offset="0" stop-color="#fff" stop-opacity=".7"/><stop offset=".1" stop-color="#aaa" stop-opacity=".1"/><stop offset=".9" stop-opacity=".3"/><stop offset="1" stop-opacity=".5"/></linearGradient><rect rx="4" width="90" height="18" fill="#555"/><rect rx="4" x="37" width="53" height="18" fill="#4c1"/><path fill="#4c1" d="M37 0h4v18h-4z"/><rect rx="4" width="90" height="18" fill="url(#a)"/><g fill="#fff" text-anchor="middle" font-family="DejaVu Sans,Verdana,Geneva,sans-serif" font-size="11"><text x="19.5" y="14" fill="#010101" fill-opacity=".3">build</text><text x="19.5" y="13">build</text><text x="62.5" y="14" fill="#010101" fill-opacity=".3">passing</text><text x="62.5" y="13">passing</text></g></svg>'

    return '<svg xmlns="http://www.w3.org/2000/svg" width="98" height="18"><linearGradient id="a" x2="0" y2="100%"><stop offset="0" stop-color="#fff" stop-opacity=".7"/><stop offset=".1" stop-color="#aaa" stop-opacity=".1"/><stop offset=".9" stop-opacity=".3"/><stop offset="1" stop-opacity=".5"/></linearGradient><rect rx="4" width="98" height="18" fill="#555"/><rect rx="4" x="37" width="61" height="18" fill="#dfb317"/><path fill="#dfb317" d="M37 0h4v18h-4z"/><rect rx="4" width="98" height="18" fill="url(#a)"/><g fill="#fff" text-anchor="middle" font-family="DejaVu Sans,Verdana,Geneva,sans-serif" font-size="11"><text x="19.5" y="14" fill="#010101" fill-opacity=".3">build</text><text x="19.5" y="13">build</text><text x="66.5" y="14" fill="#010101" fill-opacity=".3">unknown</text><text x="66.5" y="13">unknown</text></g></svg>'
