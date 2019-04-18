#!/usr/bin/env python

from jinja2 import Template

vlan_template = Template("""vlan {{id}}
 name VLAN_{{id}}""")

output = vlan_template.render(id=101)

print()
print(output)
print()