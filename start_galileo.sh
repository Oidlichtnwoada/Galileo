#!/bin/sh
rm -rf /home/pi/Galileo/__pycache__
git -C /home/pi/Galileo fetch
git -C /home/pi/Galileo pull
python3 /home/pi/Galileo/start_galileo.py
