#! /bin/bash

rm db.sqlite3
python3 manage.py makemigrations album
python3 manage.py makemigrations song
python3 manage.py makemigrations user
python3 manage.py migrate
python3 populate.py