#!/bin/bash

echo `service network-manager stop`
echo `ip link set wlan0 down`
echo `iwconfig wlan0 mode ad-hoc essid AdHocNetwork channel 11`
echo `ip link wlan0 up`
echo `dhclient wlan0`
