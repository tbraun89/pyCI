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

import tempfile
import shutil
import subprocess
import re

from pyCI.util import get_logger
from pyCI.util import DB


logger = get_logger('repository.py')


class Repository:
    UNKNOWN = 0
    VCS_ERROR = 1
    SUCCESS = 2
    FAILED = 3

    def __init__(self, db_file):
        self.db = DB(db_file)
        self.url = None
        self.name = None
        self.steps = []
        self.work_dir = tempfile.mkdtemp()
        self.log = ''
        self.branch = 'master'

    def add_step(self, step):
        self.steps.append(step)

    def execute(self):
        self.db.add_project(self.name, '', Repository.UNKNOWN)

        process = subprocess.Popen('git ls-remote --heads {0} {1}'.format(self.url, self.branch),
                                   shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()
        ret_val = process.returncode

        if ret_val == 0:
            self.__execute_steps__(out)
        else:
            logger.error('Can not check repository "{0}".'.format(self.name))
            logger.error('Connection to repository "{0}" refused.'.format(self.url))
            self.db.update_status(self.name, Repository.VCS_ERROR)

    def __execute_steps__(self, git_id):
        git_id = git_id.split('\t')[0]

        if git_id != self.db.current_git_id(self.name):
            self.db.update_git_id(self.name, git_id)
            self.steps.sort(key=lambda x: x[0])
            self.__git_clone__()
            failed = False

            for step in self.steps:
                success = self.__execute_step__(step[1])

                if not success:
                    self.log += 'Build failed.\n'
                    self.db.update_status(self.name, Repository.FAILED)
                    failed = True
                    break

            if not failed:
                self.log += 'Build successful.\n'
                self.db.update_status(self.name, Repository.SUCCESS)

            self.__clean__()

    def __git_clone__(self):
        logger.info('{0} has changed.'.format(self.name))
        logger.info('Cloning branch "{2}" of repository "{0}" to "{1}".'.format(self.url, self.work_dir, self.branch))
        process = subprocess.Popen('git clone --depth=1 --branch {1} {0} .'.format(self.url, self.branch),
                                   cwd=self.work_dir, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process.communicate()
        ret_val = process.returncode

        if ret_val != 0:
            logger.error('Can not clone branch "{1}" of repository "{0}".'.format(self.name, self.branch))
            logger.error('Connection to repository "{0}" refused.'.format(self.url))
            self.log += 'Can not clone repository from {0}.\n'.format(self.url)
            self.db.update_status(self.name, Repository.VCS_ERROR)
        else:
            self.log += 'Cloning repository from {0}.\n'.format(self.url)

    def __execute_step__(self, step):
        process = subprocess.Popen(step, cwd=self.work_dir,
                                   shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()
        ret_val = process.returncode

        logger.info('Executed "{0}" for "{1}".'.format(step, self.name))
        self.log += 'Executed ""{0}"".\n'.format(step)

        if ret_val == 0 and err == '':
            self.log += out.replace('"', '""')
            return True
        else:
            self.log += out.replace('"', '""')
            self.log += err.replace('"', '""')
            return False

    def __clean__(self):
        shutil.rmtree(self.work_dir)
        self.db.add_log(self.name, self.log)


def create_repository_list(config, database):
    repositories = []
    current = None
    repo_url = None
    repo_name = None
    repo_step = None
    repo_branch = None

    for token in config:
        if token == 'new_repo':
            current = Repository(database)
            repositories.append(current)
        elif repo_url:
            current.url = token
        elif repo_name:
            current.name = token
        elif repo_branch:
            current.branch = token
        elif repo_step is not None:
            current.add_step((repo_step, token))

        repo_url = (token == 'repo.url')
        repo_name = (token == 'repo.name')
        repo_branch = (token == 'repo.branch')

        try:
            repo_step = int(re.match('^repo.step(\d+)$', token).group(1))
        except AttributeError:
            repo_step = None

    return repositories
