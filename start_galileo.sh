#!/bin/sh
git -C /home/pi/Galileo fetch
git -C /home/pi/Galileo pull
python3 /home/pi/Galileo/galileo.py



