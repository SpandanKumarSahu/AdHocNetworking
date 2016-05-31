  How to Run :
  
        1. Place the codes in all the devices.
        2. Get into the root. ( Type sudo -i ) - Necessary because netwrok creation can only done in sudo mode.
        3. Go into the directory of the code.
        4. May have to grant permissions to all the files. So type, chmod +rwxrwxrwx *
        5. Type python Starter.py
        6. This will get you all the devices connected.
        7. Incase you want to run a server client model, we had designed one.
            In the Starter.py file, I have commented out two lines. Just uncomment them and run Starter.py again
         
Note:
        1. The server-client model was not tested well enough. It has some bugs:
            a) Untill all the clients are connected with the server, the server won't update any of the client's information.
            b) There is some algorithmic fault, that the information gets updated wrongly.
        2. Other possible errors might include:
            a) I have assumed this to be run on devices running Ubuntu 14.04. Network Manager has to be installed.
            b) python interpreter must be present
            c) This is only if you run the client-server model:
                Though by default ( in Ubuntu 14.04 ) the first IP is automatically assigned 10.42.0.1, if the starting system has 
                different IP, then open client.cpp and change 10.42.0.1 to the IP. and do the same in call_client.sh and server.cpp
                To view IP of your current connection, type ifconfig.
            d) In the rarest of the rarest case, you might be already using the same socket. In that case, simply change 17000 to any number 
                between 10000 and 50000 in both call_client.sh and call_server.sh
            e) Another assumption that all devices have wifi interface as wlan0.
                By default, it should be wlan0 and all devices presumably have this one. If you have multiple wifi devices and change it to
                something else, you may need to go through codes.

For further help:
 mail to : spandankumarsahu@gmail.com
