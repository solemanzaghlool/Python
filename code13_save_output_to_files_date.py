"""This is to write data to file and naming them as .hostname-date-command. """

from datetime import datetime
from scrapli.driver.core import IOSXEDriver

#### Make a Date/Time Variable
my_time = datetime.now().strftime("%Y-%m-%d")

##Input command from User
command = input("Enter IOS-XE command: ")

##Read file with list of devices.
with open("SupportingFiles/13/device_list.txt", "r") as f:
    device_list= f.read()

device_list_split = device_list.splitlines()

#### Scrapli connect

for host in device_list_split:
	device = {
	"host": host,
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
	rootpath = "SupportingFiles/13/"
	filename = device["host"] + '-' + my_time + '-' + command + '.ios'
	full_path = rootpath+filename
	
	with open(full_path, "x") as f:  
		for line in output_lines:
			f.write(line + '\n')