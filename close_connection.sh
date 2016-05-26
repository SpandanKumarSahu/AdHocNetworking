#!/bin/bash

echo `iwconfig wlan0 down`
echo `ip link set wlan0 down`
