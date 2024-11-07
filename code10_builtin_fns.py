""" This is to test Python built-in functions"""

import time
from rich import print as rprint

# help()
help(print)  # press q to exit help menu
print("hello", "world", sep="-")

# isinstance()
print(isinstance(3, int))
print(isinstance(3, list))

# dir()
for method in dir(list):
    print(method)

# time()
print(time.localtime())

# rich print
rprint("[red]do not login[/red]")
rprint("[red]do not login[/red]")
