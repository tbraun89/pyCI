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

from distutils.core import setup
from distutils.command.install import install
from subprocess import call
import os
import shutil

import pyCI


def __create_custom_files__():
    if not os.path.exists('/var/log/pyCI'):
        os.mkdir('/var/log/pyCI')

    if not os.path.exists('/etc/pycirc'):
        shutil.copyfile('conf/pycirc', '/etc/pycirc')

    if not os.path.exists('/etc/pyci.db'):
        shutil.copyfile('conf/pyci.db', '/etc/pyci.db')

    shutil.copyfile('conf/init.rc', '/etc/init.d/pyCI')
    call(['chmod', '755', '/etc/init.d/pyCI'])
    call(['update-rc.d', 'pyCI', 'start', '20', '3', '5', '.', 'stop', '20', '0', '1', '2', '6'])

    if not os.path.exists('/var/www/pyci'):
        os.makedirs('/var/www/pyci')

    shutil.copyfile('public/jquery.js', '/var/www/pyci/jquery.js')
    shutil.copyfile('public/pyci.js', '/var/www/pyci/pyci.js')
    shutil.copyfile('public/pyci.css', '/var/www/pyci/pyci.css')
    shutil.copyfile('public/favicon.ico', '/var/www/pyci/favicon.ico')
    call(['chown', '-R', 'www-data:www-data', '/var/www/pyci'])


def __migrate_database__():
    if os.path.exists('/etc/pyci.db'):
        import sqlite3
        from pyCI.util import slugify
        db = sqlite3.connect('/etc/pyci.db')

        with db:
            cur = db.cursor()
            cur.execute('PRAGMA table_info(project_infos)')
            db.commit()

            if 'slug' not in [i[1] for i in cur.fetchall()]:
                cur.execute('ALTER TABLE project_infos ADD COLUMN slug TEXT')
                db.commit()

                cur.execute('SELECT name FROM project_infos')
                db.commit()

                for name in [i[0] for i in cur.fetchall()]:
                    cur.execute('UPDATE project_infos SET slug="{1}" WHERE name="{0}"'.format(name, slugify(name)))
                    db.commit()


class CustomInstallCommands(install):
    def run(self):
        __migrate_database__()
        __create_custom_files__()

        install.run(self)


setup(
    name='py-ci',
    version=pyCI.VERSION,
    packages=['pyCI', 'pyCI.html', 'pyCI.util', 'pyCI.html.sites', 'pyCI.html.helper'],
    scripts=['bin/pyci.cgi', 'bin/pyci'],
    url='',
    license='GPLv2',
    author='Torsten Braun',
    author_email='tbraun@tnt-web-solutions.de',
    description='Minimalistic Python CI Server.',
    requires=['daemon', 'pysqlite'],
    cmdclass={
        'install': CustomInstallCommands
    }
)
