import subprocess
subprocess.call("./getMAC.sh",shell=True)
with open('AdHocNetwork', 'r') as myfile:
    data=myfile.readlines()
print data[9]
print data[2]
with open('MAC_file.txt', 'r') as macfile:
    mac_data=macfile.read()
mac_addr="mac-address="
dummy="HWaddr "
mac_index=mac_data.find(dummy,0,len(mac_data))
mac_addr+=mac_data[mac_index+len(dummy):mac_index+len(dummy)+17]
mac_addr+="\n"
uuid_file=open('UUID_file.txt','r')
uuid_data="uuid="+uuid_file.read()
data[9]=mac_addr
data[2]=uuid_data
uuid_file.close()

report=open('AdHocNetwork','w')
final_data=' '.join(data)
print final_data
report.write(final_data)
report.close()

