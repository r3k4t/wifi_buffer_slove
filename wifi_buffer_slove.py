import os
import sys
import time
os.system("clear")
time.sleep(1)
print ("   ####### Author : Rahat Khan Tusar(RKT) #######")
time.sleep(2)
print ("########  Github : https://github.com/r3k4t  ########")
print
gateway = raw_input("Enter your router gateway :")
os.system("ping {} -c10".format(gateway))
print
print ("Ping process is stop")
print
time.sleep(3)
print
print ("Disconnecting  ...................")
time.sleep(3)
os.system("sudo service NetworkManager stop")
print
print ("Reconnecting  ....................")
print
os.system("sudo service NetworkManager restart")
print
print ("Success.wifi speed is increasing and no buffering.")
print

