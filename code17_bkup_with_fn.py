"""This is to backup config using a created function from custom library"""

from my_bkup_fn import backup_config

HOST = "192.168.100.231"
backup_config(HOST)
