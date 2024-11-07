
from datetime import datetime
from scrapli.driver.core import IOSXEDriver

def backup_config(hostname):
    #### Make a Date/Time Variable
    my_time = datetime.now().strftime("%Y-%m-%d")

    ##Input command from User
    command = "show run"

    #### Scrapli connect
    device = {
    "host": hostname,
    "auth_username": "cisco",
    "auth_password": "cisco",
    "port": 22,
    "auth_strict_key": False,
    "ssh_config_file": True
    }
	
    with IOSXEDriver(**device) as conn:
        output = conn.send_command(command)
        output_lines = output.result.splitlines()
	

    ## Write output to file	
    rootpath = "SupportingFiles/17/"
    filename = device["host"] + '-' + my_time + '-' + command + '.ios'
    full_path = rootpath+filename
	
    with open(full_path, "x") as f:  
        for line in output_lines:
            f.write(line + '\n')