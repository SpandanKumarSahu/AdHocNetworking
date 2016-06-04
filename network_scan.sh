#!/bin/bash

sudo ifconfig wlan0 down
sudo stop network-manager
echo `sleep 3`
sudo start network-manager
sudo ifconfig wlan0 up
sleep 10
echo `iwlist wlan0 scan > NetworkScan.txt`
