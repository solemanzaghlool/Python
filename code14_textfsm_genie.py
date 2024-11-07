"""This is to output structured data using scrapli/textfsm.
to install use: pip3 install scrapli[textfsm] 
to install geneie use: pip3 install scrapli[genie]"""

import json
from scrapli.driver.core import IOSXEDriver

device = {
    "host": "192.168.100.231",
    "auth_username": "cisco",
    "auth_password": "cisco",
    "port": 22,
    "auth_strict_key": False,
    "ssh_config_file": True,
}

with IOSXEDriver(**device) as conn:
    response = conn.send_command("show version")
    textfsm_result = json.dumps(response.textfsm_parse_output(), indent=4)
    genie_result = json.dumps(response.genie_parse_output(), indent=4)
    genie_serial_number = response.genie_parse_output()
    print(
        "\n", "The chassis S/N is:", genie_serial_number["version"]["chassis_sn"], "\n"
    )

print(textfsm_result)
print(genie_result)

with IOSXEDriver(**device) as conn:
    response = conn.send_command("show ip interface brief")
    textfsm_result = json.dumps(response.textfsm_parse_output(), indent=4)
    genie_result = json.dumps(response.genie_parse_output(), indent=4)

print(textfsm_result)
print(genie_result)
