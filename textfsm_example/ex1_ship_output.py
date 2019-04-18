#!/usr/bin/env python

import textfsm
from pprint import pprint

file = open ('ex1_ship_output.txt', 'r')
show_output = file.read()

template = open('ex1_ship_template.textfsm')
re_table = textfsm.TextFSM(template)
results = re_table.ParseText(show_output)

pprint(results)
