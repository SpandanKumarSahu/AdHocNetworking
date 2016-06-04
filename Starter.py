#!/usr/bin/python

import subprocess
import sys

def isNetworkAvailable (report):
    if 'AdHocNetwork' in report.read():
        return True
    else:
        return False

print "start"
subprocess.call("./clear_mess.sh",shell=True)
subprocess.call("./network_scan.sh",shell=True)
report=open('NetworkScan.txt','r')
if isNetworkAvailable(report):
    subprocess.call("./connect_to_existing_network.sh",shell=True)
    print "Connected to Network"
    #subprocess.call("./call_client.sh",shell=True)
else:
    print "Here it goes for creating a new connection"
    try:
        subprocess.call("./create_new_adHoc_network.sh",shell=True)
    except Error:
        print "Cannot Create"
        sys.exit(0)
    print "Created new AdHoc Network"
    #subprocess.call("./call_server.sh",shell=True)
report.close()
print "end"
