from rich import print as rprint
from napalm import get_network_driver

device = {
    "hostname": '192.168.100.231', 
    "username": "cisco",
    "password": "cisco",
    "driver": "ios"
    }

driver = get_network_driver(device["driver"])

with driver(username=device["username"], password=device["password"], hostname=device["hostname"]) as device:
    result_facts = device.get_facts()
    result_interface = device.get_interfaces()

rprint(result_facts)
rprint(result_interface)
print (result_facts["vendor"]*20, "\n")