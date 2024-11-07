import sys
from my_functions import adder

paths = sys.path
for path in paths:
    print(path)  #directories of where you can import .py files


adder(1,5)