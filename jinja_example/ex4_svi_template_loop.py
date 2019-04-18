#!/usr/bin/env python

from jinja2 import Template

vlans = [
    {'name:': 'VLAN_101',
     'vlan_var': 101,
     'ip_var': '192.168.1.1',
     'mask_var': '255.255.255.0'},
    {'name:': 'VLAN_201',
     'vlan_var': 201,
     'ip_var': '172.16.20.1',
     'mask_var': '255.255.0.0'},
    {'name:': 'VLAN_301',
     'vlan_var': 301,
     'ip_var': '10.0.0.0',
     'mask_var': '255.0.0.0'}
]

with open("ex4_svi_template_loop.j2") as f:
    config_in = Template(f.read())

config_out = config_in.render(vlans=vlans)

print ("!Generating Output for Multiple VLANs")
print(config_out)