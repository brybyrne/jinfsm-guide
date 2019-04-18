#!/usr/bin/env python

from netmiko import ConnectHandler
import textfsm
from pprint import pprint
from device_details import ios_xe1, ios_xe2

with open("ex2_ship_template.textfsm") as f:
    re_table = textfsm.TextFSM(f)

with ConnectHandler(device_type='cisco_ios',
                    ip=ios_xe1['address'],
                    username=ios_xe1['username'],
                    password=ios_xe1['password'],
                    port=ios_xe1['port']) as ch:

    ship_output = ch.send_command("show ip interface brief")

    results = re_table.ParseText(ship_output)

for interface in results:
    if interface[2]!="up":
        print("Warning: " + interface[0] + " is currently in the " + interface[2] + " state.")
        print("Someone should probably do something.")
        print()
    else:
        print("Good Job! " + interface[0] + " is up. Nothing to see here!")
        print()


