#!/bin/sh
/home/pi/Galileo/update_pi.sh
git -C /home/pi/Galileo fetch
git -C /home/pi/Galileo pull
python3 /home/pi/Galileo/start_galileo.py
