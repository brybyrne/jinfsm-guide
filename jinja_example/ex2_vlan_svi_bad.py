#!/usr/bin/env python

from jinja2 import Template

vlan_var = 101
svi_ip = '192.168.1.1'
svi_mask = '255.255.255.0'


vlan_template = Template('vlan {{id}} \n'
                        ' name VLAN_{{id}}')

svi_template = Template('interface vlan {{id}} \n'
                        ' description This is the SVI for VLAN {{id}} \n'
                        ' ip address {{address}} {{mask}}')

vlan_output = vlan_template.render(id=vlan_var)

svi_output = svi_template.render(id=vlan_var, address=svi_ip, mask=svi_mask)

print()
print('!Output from vlan_template')
print(vlan_output)
print()
print('!Output from SVI'
      ' template')
print(svi_output)
print()