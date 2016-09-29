#!/usr/bin/env bash
# Script to set up plenario  on Vagrant.
set -e

echo "-------------------- Apt-get update and install dependencies -------------------- "

sudo apt-get update -y
sudo apt-get install -y redis-server curl git python-pip gdal-bin libpq-dev libgeos-dev python-pip postgresql postgresql-client-common postgresql-client postgis

echo "-------------------- Clone plenario.git -------------------- "

git clone https://github.com/UrbanCCD-UChicago/plenario
cd plenario

echo "-------------------- Make plenario virtualenv and pip install requirements.txt -------------------- "

virtualenv plenario
pip install -r requirements.txt

echo "-------------------- creating postgres user, database to match settings.py -------------------- "

sudo -u postgres psql -c "ALTER USER "postgres" WITH PASSWORD 'password';"
sudo -u postgres createdb -O postgres plenario_test

echo "-------------------- creating postgres POSTGIS extension -------------------- "

sudo -u postgres psql plenario_test -c "CREATE EXTENSION postgis;"

echo "-------------------- You might need to edit plenario/settings.py and add your AWS credentials -------------------- "

echo "-------------------- Starting redis-server in background -------------------- "

redis-server &

echo "-------------------- Running python init_db.py to seed db -------------------- "

python init_db.py

echo "-------------------- Running Flask app -------------------- "

python runserver.py &

echo "-------------------- Open http://localhost:5000/ on your host or curl localhost:5000 in vagrant vm -------------------- "
