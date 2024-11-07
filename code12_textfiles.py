"""These are examples for manipulating text files"""

##Reading files "r" ##

with open("SupportingFiles/12/file1.txt", "r") as f:
    x = f.read()  ##reads entire file and returns as string
    print(x, "\n")

with open("SupportingFiles/12/file1.txt", "r") as f:
    x = f.read(12)  ##reads first 12 character
    print(x, "\n")

with open("SupportingFiles/12/file1.txt", "r") as f:
    x = f.readlines()  ##goes through line by line in and puts in list
    print(x, "\n")
    for line in x:
        print(line)

##Writin files - "w" will erase existing data in a file "a" will append data,
# "x" creates a new file and writes##

with open("SupportingFiles/12/file2.txt", "w") as f:
    f.write("This is new text\n")

with open("SupportingFiles/12/file2.txt", "a") as f:
    f.write("This is new text\n")

with open("SupportingFiles/12/file3.ios", "w") as f:  ## "x" creates new file and writes
    my_list = [
        "enable\n",
        "conf t\n",
        "interface GigabitEthernet0/0\n",
        " no shutdown\n",
    ]
    print(my_list)
    f.writelines(my_list)

with open("SupportingFiles/12/file3.ios", "r") as f:
    x = f.read()
    print(x, "\n")
