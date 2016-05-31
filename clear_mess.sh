#!/bin/bash

sudo ifconfig wlan0 down
sudo stop network-manager
sudo rm /etc/NetworkManager/system-connections/AdHocNetwork
sudo sleep 15
sudo start network-manager
sleep 15
sudo ifconfig wlan0 up






