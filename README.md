# pyCI - a minimal CI server

pyCI is a minimal CI server with web interface and a commandline
runner for small systems like `A10-OLinuXino-LIME` or `Raspberry Pi`
that have not much resources.

The server monitors the Git repositories of your configured projects
and starts a new build if there was a change. If the return value of
a build step is not `0` or there are messages logged in `stderr` the
build will fail.

All logs of `stdout` and `stderr` are stored for each build an can be
displayed in the web interface.

## Requirements

* Python 2.7.x
* Python `daemon` library
* Python `pysqlite` library

## Installation

### pyCI

* clone the Git repository
* run `sudo python setup.py install`
* edit the `/etc/pycirc` file and add your projects
* start the service with `sudo service pyCI start`

An init script will be automatically added on install. The asserts
for the web interface are copied to `/var/www/pyci` and owned by the
user and group `www-data`.

### Web Interface (Nginx + fcgiwrap)

* create a new server file under `/etc/nginx/sites-available`
* create a symbolic link to the server file in `/etc/nginx/sites-enabled`
* configure the server

<b></b>

    server {
    	listen      80;
    	server_name SERVER_NAME;
    
	    location ~* ^.+\.(css|png|ico|js)$ {
	        root    /var/www/pyci;
		    expires 30d;
	    }    
    
        location / {
    	    fastcgi_pass  unix:/var/run/fcgiwrap.socket;
    	    fastcgi_param SCRIPT_FILENAME /usr/local/bin/pyci.cgi;
    	    fastcgi_param PATH_INFO $uri;
    	    fastcgi_param QUERY_STRING $args;
	    }
    }

## Configuration

The configuration is stored in `/etc/pycirc` with an example.


    start_config                       start the global server configuration section
    config.build_success=command       run "command" after a successful build
    config.build_failed=command        run "command" after a failed build
    config.vcs_error=command           run "command" if pyCI can not connect to the VCS
                                       "command" if all status are unknown
    
    new_repo                           start a new project configuration section
    repo.url=URL_TO_GIT                url to the remote git repository
    repo.name=My Project               unique name of the project
    repo.step0=command                 "command" executed in the first build step
    repo.step1=command                 "command" executed in the second build srep
    repo.step2=...

## Running the Tests

To run the tests you just have to change to the test folder and run the `suite.py` file.

    cd tests
    python suite.py

## Contributing

1. Fork it (https://github.com/tbraun89/pyCI/fork)
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Add your feature and don't forget the tests
4. Commit your changes (`git commit -am 'Add some feature'`)
5. Push to the branch (`git push origin my-new-feature`)
6. Create a Pull Request
