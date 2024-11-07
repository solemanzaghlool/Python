"""These are examples making for loops"""

routes = ["192.168.1.0/30", "192.168.5.0/24", "10.10.0.0/16", "1.1.1.0/24"]

for route in routes:
    print(f"my subnet is {route}")

##using the range function

for x in range(0, len(routes)):
    print(routes[x])
for x in range(0, len(routes), 2):
    print(routes[x], "------step2")

##Nested loop example
device_list = ["R1", "R2", "R3"]
interface_list = ["gi0/1", "gi0/2", "gi0/3"]

for device in device_list:
    print(f"*** Device {device}")
    for interface in interface_list:
        print(f"****** interface {interface}")

print("\n")

##Using 'continue' operator to skip interation
device_list = ["R1", "R2", "R3"]
interface_list = ["gi0/1", "gi0/2", "gi0/3"]

for device in device_list:
    if device == "R2":
        print("\n**********SKIPPING R2************\n")
        continue

    print(f"*** Device {device}")
    for interface in interface_list:
        print(f"****** interface {interface}")

##Using 'break' operator to exit for loop
device_list = ["R1", "R2", "R3"]
interface_list = ["gi0/1", "gi0/2", "gi0/3"]

for device in device_list:
    if device == "R2":
        print("\n**********BREAKING************\n")
        break

    print(f"*** Device {device}")
    for interface in interface_list:
        print(f"****** interface {interface}")
