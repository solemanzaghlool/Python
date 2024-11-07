"""This is to demonstrate httpx Library"""

import json
import httpx
from rich import print as rprint

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}
HOST = "192.168.100.239"

BASE_URL = f"https://{HOST}/restconf/data/"
TREE_URL = "Cisco-IOS-XE-arp-oper:arp-data"
FULL_URL = BASE_URL + TREE_URL


with httpx.Client(verify=False) as client:
    response = client.get(FULL_URL, headers=headers, auth=("cisco", "cisco"))

print("\n", response)
print("\n", response.text)
print("\n", type(response.text))

response_dict = json.loads(response.text)
print("\n", type(response_dict))
rprint(response_dict)
