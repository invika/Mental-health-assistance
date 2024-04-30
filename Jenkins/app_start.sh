#!/bin/bash
source /home/ubuntu/Mental-health-assistance/mental_health_care/bin/activate
python3.11 -m pip install channels
sudo apt install mesa-utils

export TF_ENABLE_ONEDNN_OPTS=0

echo "Running the Migrations"
python3.11 /home/ubuntu/Mental-health-assistance/manage.py migrate

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
python3.11 /home/ubuntu/Mental-health-assistance/manage.py runserver 0.0.0.0:8000 > /home/ubuntu/Mental-health-assistance/logs/server.log 2>&1