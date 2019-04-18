#!/usr/bin/env python

from jinja2 import Template
import yaml
from argparse import ArgumentParser
from pprint import pprint

parser = ArgumentParser("Specifying the YAML File")
parser.add_argument("-f", "--file",
                    help="Please Specify the YAML file.",
                    required=True)
args = parser.parse_args()
file_name = args.file

with open(file_name) as f:
    yaml_data = yaml.safe_load(f.read())

with open("ex6_yaml_data.j2") as f:
    config_in = Template(f.read())

for device in yaml_data["devices"]:
    config_out = config_in.render(interfaces=device["interfaces"],
                                  file=file_name)

print(config_out)



