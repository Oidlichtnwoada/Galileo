#!/bin/sh
sudo systemctl restart galileo.service
sleep 10
sudo systemctl status galileo.service
