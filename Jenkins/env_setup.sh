#!/bin/bash

#sudo apt install python3-full -S
#sudo apt install -y python3.11-venv -S


#python3.11 -m ensurepip --upgrade
#python3.11 -m pip install --upgrade pip
#sudo apt install python3-virtualenv -S

#Creating virtual environment
python3.11 -m venv mental_health_care
#virtualenv mental_health_care --python=python3.12

#Running python virtual environment
source mental_health_care/bin/activate


#virtualenv --upgrade-embed-wheels
#virtualenv --reset-app-data mental_health_care
python3.11 -m pip install --upgrade pip
python3.11 -m pip install setuptools
python3.11 -m pip install --upgrade setuptools

echo `pwd`
echo "$USER"
#sudo apt install python3.11-full -S
#sudo apt install python3.11.12-dev -S
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