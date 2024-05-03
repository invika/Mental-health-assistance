#!/bin/bash
source /home/ubuntu/Mental-health-assistance/mental_health_care/bin/activate
python3 -m pip install channels
sudo apt install mesa-utils

export TF_ENABLE_ONEDNN_OPTS=0

echo "Running the Migrations"
python3 /home/ubuntu/Mental-health-assistance/manage.py migrate

#!/bin/bash

# Check if port 8000 is open
if lsof -Pi :8000 -sTCP:LISTEN -t >/dev/null; then
    # Port is open, find and kill the process
    PID=$(lsof -ti :8000)
    echo "Port 8000 is open, killing process $PID"
    kill $PID
else
    # Port is not open
    echo "Port 8000 is not open"
fi

#starting the server....
echo "Running the application on 8000 port"
nohup python3 /home/ubuntu/Mental-health-assistance/manage.py runserver 0.0.0.0:8000 &

# Check if port 5500 is open
if lsof -Pi :5500 -sTCP:LISTEN -t >/dev/null; then
    # Port is open, find and kill the process
    PID=$(lsof -ti :5500)
    echo "Port 5500 is open, killing process $PID"
    kill $PID
else
    # Port is not open
    echo "Port 5500 is not open"
fi

cd /home/ubuntu/Mental-health-assistance/facefilters
npm install
nohup nodejs index.js &