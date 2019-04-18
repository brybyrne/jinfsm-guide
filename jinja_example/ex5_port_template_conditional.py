#!/usr/bin/env python

from jinja2 import Template

ports = [
    {'name': 'GigabitEthernet0/0/1',
     'mode': 'access',
     'vlan': 101,
     'state': 'enabled'},
    {'name': 'GigabitEthernet0/0/2',
     'mode': 'access',
     'vlan': 201,
     'state': 'shutdown'},
    {'name': 'GigabitEthernet0/0/3',
     'mode': 'access',
     'vlan': 301,
     'state': 'up'},
    {'name': 'GigabitEthernet0/0/4',
     'mode': 'routed',
     'vlan': ''},
    {'name': 'GigabitEthernet0/0/24',
     'mode': 'trunk',
     'allowed': '101,201,301'}
]

with open("ex5_port_template_conditional.j2") as f:
    config_in = Template(f.read())

config_out = config_in.render(ports=ports)

print(config_out)