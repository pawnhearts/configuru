#!/usr/bin/env bash

python myapp.py

DB_URL=sqlite://foo python myapp.py

echo 'DB_URL=mysql://mysql/db' >.env
python myapp.py
rm .env


