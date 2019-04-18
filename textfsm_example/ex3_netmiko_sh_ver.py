#!/usr/bin/env python

from netmiko import ConnectHandler
import os
import yaml

device_outputs = []

with open("device_details.yaml") as f:
    config = yaml.full_load(f.read())

env = config["env_path"]

os.environ['NET_TEXTFSM'] = env

for device in config["devices"]:

    with ConnectHandler(device_type='cisco_ios', ip=device["address"], username=device["username"],
                        password=device["password"], port=device["ssh_port"]) as ch:

        sh_ver_output = ch.send_command("show version",
                                        use_textfsm=True)

        for line in sh_ver_output:
            print()
            print("==========================================")
            print("For device: {} ".format(line["hostname"]))
            print("The serial number is: {}".format(line["serial"]))
            print("The IOS Version is: {}".format(line["version"]))
            print("The uptime is: {}".format(line["uptime"]))
            print("==========================================")


