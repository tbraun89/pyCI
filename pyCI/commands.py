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

import subprocess
from pyCI.util import get_logger


logger = get_logger('commands.py')


def __execute_command__(command):
    if command is not None:
        process = subprocess.Popen(command,
                                   shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()
        ret_val = process.returncode

        logger.info('Executed "{0}" ({1}).'.format(command, ret_val))

        if ret_val == 0:
            logger.info(out)
        else:
            logger.error(err)


def build_success_command(config):
    command = None

    for i, token in enumerate(config):
        if token == 'config.build_success':
            command = config[i+1]

    __execute_command__(command)


def build_failed_command(config):
    command = None

    for i, token in enumerate(config):
        if token == 'config.build_failed':
            command = config[i+1]

    __execute_command__(command)


def vcs_error_command(config):
    command = None

    for i, token in enumerate(config):
        if token == 'config.vcs_error':
            command = config[i+1]

    __execute_command__(command)
