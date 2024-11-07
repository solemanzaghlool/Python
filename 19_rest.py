from rich import print as rprint
import httpx
import json


headers = {"Accept" : "application/yang-data+json", "Content-Type" : "application/yang-data+json"}
auth = httpx.BasicAuth(username="cisco", password="cisco")
host = "192.168.100.239"

base_url = f"https://{host}/restconf/data/"
tree_url = "Cisco-IOS-XE-arp-oper:arp-data"
full_url = base_url+tree_url


with httpx.Client(verify=False) as client:
    response = client.get(full_url, headers=headers, auth=auth)

print('\n',response)
print('\n',response.text)
print('\n',type(response.text))

response_dict = json.loads(response.text)
print('\n',type(response_dict))
rprint(response_dict)