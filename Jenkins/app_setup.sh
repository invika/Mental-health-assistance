#!/bin/bash
sudo apt update -y
sudo apt upgrade -y

#Installing Django
sudo apt install django

#Installing opencv-python-headless keras tensorflow
python3.11 -m pip install opencv-python-headless keras tensorflow django