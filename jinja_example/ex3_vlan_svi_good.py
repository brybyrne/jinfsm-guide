#!/usr/bin/env python

from jinja2 import Template

vlan_var = 101
svi_ip = '192.168.1.1'
svi_mask = '255.255.255.0'

with open("ex3_vlan_template.j2") as f:
    vlan_in_temp = Template(f.read())

with open("ex3_svi_template.j2") as f:
    svi_in_temp = Template(f.read())

vlan_output = vlan_in_temp.render(id=vlan_var)

svi_output = svi_in_temp.render(id=vlan_var, ip=svi_ip, mask=svi_mask)

print()
print('!Output from vlan_template')
print(vlan_output)
print()
print('!Output from SVI template')
print(svi_output)
print()

