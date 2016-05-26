#!/usr/bin/python

import subprocess

def isNetworkAvailable (report):
    if 'AdHocNetwork' in report.read():
        return True
    else:
        return False

def check_if_properly_connected(mode):
    subprocess.call("./check_connection.sh",shell=True)
    report=open('CurrentConnection.txt','r')
    if isNetworkAvailable(report):
        return
    else:
        if mode==0:
            subprocess.call("./connect_to_existing_network.sh",shell=True)
        else:
            subprocess.call("./create_new_adHoc_network.sh",shell=True)
    

print "start"
subprocess.call("./network_scan.sh",shell=True)
report=open('NetworkScan.txt','r')
if isNetworkAvailable():
    subprocess.call("./connect_to_existing_network.sh",shell=True)
    check_if_properly_connected(0)
    print "Connected to Network"
    subprocess.call("./call_client.sh",shell=True)
else:
    subprocess.call("./create_new_adHoc_network.sh",shell=True)
    check_if_properly_connected(1)
    print "Created new AdHoc Network"
    subprocess.call("./call_server.sh",shell=True)
scan_report.close()
print "end"
