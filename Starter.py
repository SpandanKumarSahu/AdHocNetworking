#!/usr/bin/python

import subprocess
import sys
import os

def isNetworkAvailable (report):
    if 'AdHocNetwork' in report.read():
        return True
    else:
        return False

print "start"
os.system("sudo rm /etc/NetworkManager/system-connections/AdHocNetwork")
os.system("sudo ifconfig wlan0 down")
os.system("sudo stop network-manager")
os.system("sleep 3")
os.system("sudo start network-manager")
os.system("sudo ifconfig wlan0 up")
os.system("sleep 10")
os.system("iwlist wlan0 scan > NetworkScan.txt")
report=open('NetworkScan.txt','r')
if isNetworkAvailable(report):
    os.system("nmcli dev wifi connect AdHocNetwork")
    print "Connected to Network"
    #subprocess.call("./call_client.sh",shell=True)
else:
    print "Here it goes for creating a new connection"
    try:
        os.system("python initialize_new_AdHocFile.py")
        os.system("cp AdHocNetwork /etc/NetworkManager/system-connections")
        os.system("stop network-manager")
        os.system("sleep 7")
        os.system("start network-manager")
        os.system("sleep 7")
        os.system("nmcli con up id AdHocNetwork")
    except Error:
        print "Cannot Create"
        sys.exit(0)
    print "Created new AdHoc Network"
    #subprocess.call("./call_server.sh",shell=True)
report.close()
print "end"
