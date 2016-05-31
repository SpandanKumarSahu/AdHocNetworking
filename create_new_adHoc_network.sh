#!/bin/bash

echo `python initialize_new_AdHocFile.py`
echo `cp AdHocNetwork /etc/NetworkManager/system-connections`
echo `stop network-manager`
echo `sleep 7`
echo `start network-manager`
echo `sleep 7`
echo `nmcli con up id AdHocNetwork`
