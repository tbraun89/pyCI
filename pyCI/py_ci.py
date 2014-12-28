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

from optparse import OptionParser
from pyCI.util import get_logger
import errno
import os

from pyCI.util import tokenize_config, DB
from pyCI import build_success_command, build_failed_command, vcs_error_command
from pyCI import Repository, create_repository_list


VERSION = '0.1.0'


logger = get_logger('py_ci.py')

parser = OptionParser()
parser.add_option('-c', '--config', action='store', type='string', dest='config_file',
                  help='path to the configuration file', default='/etc/pycirc')
parser.add_option('-d', '--database', action='store', type='string', dest='database',
                  help='the database file to store the project information', default='/etc/pyci.db')
options, _ = parser.parse_args()


def main():
    db = DB(options.database)

    try:
        config = tokenize_config(options.config_file)
    except IOError:
        logger.error('Config file "{0}" not found.'.format(options.config_file))
        logger.critical('Exiting: {0}.'.format(os.strerror(int(errno.EIO))))
        exit(errno.EIO)

    for repository in create_repository_list(config, options.database):
        repository.execute()

    status_list = [i[2] for i in db.project_list()]

    if Repository.VCS_ERROR in status_list or Repository.UNKNOWN in status_list:
        vcs_error_command(config)
    elif Repository.FAILED in status_list:
        build_failed_command(config)
    elif Repository.SUCCESS in status_list:
        build_success_command(config)
    else:
        logger.warning('Status list is empty.')

    Repository.status = []


def html():
    from pyCI.html import generate_html
    generate_html()
