#!/usr/bin/env python
from __future__ import print_function, unicode_literals
#TAKES 6 SECONDS TO RUN THE FULL SCRIPT WHICH ALLOWS US TO RUN THIS SCRIPT EVERY 10 SECONDS#
# Netmiko is the same as ConnectHandler
from netmiko import Netmiko
from getpass import getpass
import time


def my_device1():
    my_device = {
        "host": "ippppppppp",
        "username": "usernameeee",
        "password": "passssss",
        "device_type": "cisco_ios",
    }

    net_connect = Netmiko(**my_device)

    output = net_connect.send_command("show ip dhcp binding")
    print(output, file=open("DHCP.html", "w"))
    
    net_connect.disconnect()
    time.sleep(10)
    my_device1()
my_device1()
