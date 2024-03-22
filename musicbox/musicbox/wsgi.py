# This file contains the WSGI configuration required to serve up your
# web application at http://wad2.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#
# The below has been auto-generated for your Django project

import os
import sys

# add your project directory to the sys.path
# change wad2 to your PythonAnywhere username
path = '/home/usmaanwahab/django_project'
if path not in sys.path:
    sys.path.append(path)

# IMPORTANTLY GO TO THE PROJECT DIR
os.chdir(path)

# set environment variable to tell django where your settings.py is
os.environ['DJANGO_SETTINGS_MODULE'] = 'musicbox.settings'

# IMPORT THE DJANGO SETUP - NEW TO 1.7
import django
django.setup()

# serve django via WSGI
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
