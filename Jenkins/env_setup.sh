#!/bin/bash

#Creating virtual environment
python3 -m venv /home/ubuntu/Mental-health-assistance/mental_health_care

#Running python virtual environment
source /home/ubuntu/Mental-health-assistance/mental_health_care/bin/activate

python3 -m pip install -r /home/ubuntu/Mental-health-assistance/Jenkins/requirements.txt
# sudo apt-get install libmysqlclient-dev build-essential pkg-config

if [ -d "logs" ] 
then
    echo "Log folder exists." 
else
    mkdir /home/ubuntu/Mental-health-assistance/logs
    touch /home/ubuntu/Mental-health-assistance/logs/server.log /home/ubuntu/Mental-health-assistance/logs/setup.log
fi

sudo chmod -R 777 /home/ubuntu/Mental-health-assistance/logs