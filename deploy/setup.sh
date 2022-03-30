#!/usr/bin/env bash

set -e

# TODO: Set to URL of git repo.
PROJECT_GIT_URL='https://github.com/himalczyk/python_django_rest_api.git'

# directory stored on the server
PROJECT_BASE_PATH='/usr/local/apps/profiles-rest-api'

# echo, type a message and install reqs
echo "Installing dependencies..."
apt-get update
# python3, venv, sqlite, nginx web server proxy to wsgi service that is going to run in supervisor
apt-get install -y python3-dev python3-venv sqlite python-pip supervisor nginx git

# Create project directory, to store the project files
mkdir -p $PROJECT_BASE_PATH
# clone project to the directory
git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH

# Create virtual environment on the server
mkdir -p $PROJECT_BASE_PATH/env
python3 -m venv $PROJECT_BASE_PATH/env

# Install python packages
$PROJECT_BASE_PATH/env/bin/pip install -r $PROJECT_BASE_PATH/requirements.txt
# python daemon for running python code as a web server
$PROJECT_BASE_PATH/env/bin/pip install uwsgi==2.0.18

# Run migrations and collectstatic
cd $PROJECT_BASE_PATH
$PROJECT_BASE_PATH/env/bin/python manage.py migrate
# collect static, gather all static files for all of the apps into one directory, store all of them to serve css, js for the django admin and rest framework
$PROJECT_BASE_PATH/env/bin/python manage.py collectstatic --noinput

# Configure supervisor is an app on linux that allows to manage processes
# copy the confing file into the location where the supervisor is kept
# reread to update the supervisor config file
# update to update processes
# restart to make sure service is started
cp $PROJECT_BASE_PATH/deploy/supervisor_profiles_api.conf /etc/supervisor/conf.d/profiles_api.conf
supervisorctl reread
supervisorctl update
supervisorctl restart profiles_api

# Configure nginx, web server to serve the static files
# need to create a location, for the config file and copy the config added (nginx_profiles_api.conf) into /etc/nginx/sites-available/profiles_api.conf
cp $PROJECT_BASE_PATH/deploy/nginx_profiles_api.conf /etc/nginx/sites-available/profiles_api.conf
# remove default config
rm /etc/nginx/sites-enabled/default
# add symbolic link sites available to sites enabled to enalbe site
ln -s /etc/nginx/sites-available/profiles_api.conf /etc/nginx/sites-enabled/profiles_api.conf
# restart system to run the changes
systemctl restart nginx.service

echo "DONE! :)"
