#!/usr/bin/env python

import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://127.0.0.1:2125/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet2"

payload = "{\"ietf-interfaces:interface\"" \
          ": {\"name\": \"GigabitEthernet2\",\"type\": \"iana-if-type:ethernetCsmacd\",\"enabled\": true,\"" \
          "ietf-ip:ipv4\": {\"address\": [{\"ip\": \"192.168.185.1\",\"netmask\": \"255.255.255.0\"}]}," \
          "\"ietf-ip:ipv6\": {}}}"
headers = {
    'Content-Type': "application/yang-data+json",
    'Accept': "application/yang-data+json",
    'Authorization': "Basic dmFncmFudDp2YWdyYW50",
    }

response = requests.request("PUT", url, data=payload, headers=headers, verify=False)

print(response.text)