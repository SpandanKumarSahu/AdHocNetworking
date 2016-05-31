#!/usr/bin/python

import subprocess

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
    subprocess.call("./create_new_adHoc_network.sh",shell=True)
    print "Created new AdHoc Network"
    #subprocess.call("./call_server.sh",shell=True)
report.close()
print "end"
