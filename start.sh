#!/bin/bash

./vlc-server.sh &
sleep 2
python vlc-client.py "/home/pi/Desktop/workout/test.mp4" 25