#!/bin/bash

#Creating virtual environment
python3.11 -m venv mental_health_care

#Running python virtual environment
source mental_health_care/bin/activate


python3.11 -m pip install --upgrade pip
python3.11 -m pip install setuptools
python3.11 -m pip install --upgrade setuptools

echo `pwd`
echo "$USER"
echo `python3.11 --version`
python3.11 -m pip install -r /var/lib/jenkins/workspace/Mental-Health-Assistance/Jenkins/requirements.txt
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config
python3.11 -m pip install mysqlclient
python3.11 -m pip install channels


if [ -d "logs" ] 
then
    echo "Log folder exists." 
else
    mkdir logs
    touch logs/server.log logs/setup.log
fi

sudo chmod -R 777 logs