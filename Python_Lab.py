#pythonR1script1.py
import getpass
import sys
import telnetlib

HOST = "192.168.122.22"
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("enable\n")
tn.write("cisco\n")
tn.write("conf t\n")
tn.write("int loop 0\n")
tn.write("ip address 1.1.1.1 255.255.255.255\n")
tn.write("end\n")
tn.write("exit\n")

print tn.read_all()

#pythonS1script1.py
import getpass
import sys
import telnetlib

HOST = "192.168.122.72"
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("enable\n")
tn.write("cisco\n")
tn.write("conf t\n")
tn.write("vlan 2\n")
tn.write("name Python_VLAN_2\n")
tn.write("vlan 3\n")
tn.write("name Python_VLAN_3\n")
tn.write("vlan 4\n")
tn.write("name Python_VLAN_4\n")
tn.write("vlan 5\n")
tn.write("name Python_VLAN_5\n")
tn.write("vlan 6\n")
tn.write("name Python_VLAN_6\n")
tn.write("end\n")
tn.write("exit\n")

print tn.read_all()


#S1script2.py
#!/usr/bin/env python

import getpass
import sys
import telnetlib

HOST = "192.168.122.72"
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("conf t\n")

for n in range (2,20):
        tn.write("vlan " + str(n) + "\n")
        tn.write("name Python_VLAN_" + str(n) + "\n")

tn.write("end\n")
tn.write("exit\n")

print tn.read_all()


#S1script3.py
#!/usr/bin/env python

import getpass
import sys
import telnetlib

user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

for n in range (72,77):
    print "Telnet to host" + str(n)
    HOST = "192.168.122." + str(n)
    tn = telnetlib.Telnet(HOST)

    tn.read_until("Username: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")

    tn.write("conf t\n")

    for n in range (2,11):
        tn.write("vlan " + str(n) + "\n")
        tn.write("name Python_VLAN_" + str(n) + "\n")

    tn.write("end\n")
    tn.write("wr\n")
    tn.write("exit\n")

    print tn.read_all()


#switchloopfile.py
#!/usr/bin/env python

import getpass
import sys
import telnetlib

user = raw_input("Enter your username: ")
password = getpass.getpass()

f = open ('myswitches')

for line in f:
    print "Configuring Switch " + (line)
    HOST = line.strip()
    tn = telnetlib.Telnet(HOST)

    tn.read_until("Username: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")

    tn.write("conf t\n")

    for n in range (2,26):
        tn.write("vlan " + str(n) + "\n")
        tn.write("name Python_VLAN_" + str(n) + "\n")

    tn.write("end\n")
    tn.write("wr\n")
    tn.write("exit\n")

    print tn.read_all()


#getconfigs.py
#!/usr/bin/env python

import getpass
import telnetlib

#Ask for username and password
user = raw_input("Enter your username: ")
password = getpass.getpass()

#open a file called myswitches
f = open ("myswitches")

#Telnet to switches and get the running configs
for line in f:
    print "Getting running config from Switch " + (line)
    HOST = line.strip()
    tn = telnetlib.Telnet(HOST)

    tn.read_until("Username: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")

    tn.write("terminal length 0\n")
    tn.write("show run\n")
    tn.write("exit\n")

    readoutput = tn.read_all()
    saveoutput = open("Switch_" + HOST, "w")
    saveoutput.write(readoutput)
    saveoutput.close



