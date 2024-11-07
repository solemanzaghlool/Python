"""These are examples of manipulating lists"""

routes = ["192.168.1.0/30", "192.168.5.0/24", "10.10.0.0/16"]
print("\n")

# Selecting Route from list
print(routes[0])
print(routes[1])
print(routes[2])
print("\n")

# Selecting Route from list in reverse
print(routes[-1])
print(routes[-2])
print(routes[-3])
print("\n")

# List for loop
for route in routes:
    print(route)
print("\n")

# Appending on a list
routes.append("1.1.1.1/32")
routes.append("2.2.2.2/32")
print(routes)

# Popping a list
routes.pop()
print(routes)

routes.pop(2)
print(routes)

routes.pop(0)
print(routes)

# Removing based on actual value (not position)
routes.remove("1.1.1.1/32")
print(routes)


# Clear a list
routes.clear()
print(routes)

#### Slicing lists:
vlans = ["10", "20", "30", "40", "50", "60", "70", "80"]
vlans_10_40 = vlans[0:4]
vlans_50_80 = vlans[4:]
print(vlans_10_40)
print(vlans_50_80)

# Slice with increment 2
vlans_odd = vlans[::2]
print(vlans_odd)

# Max and Min of list
vlans = [10, 11, 54, 12, 100, 2]
print(max(vlans), min(vlans))

# sort a list
vlans.sort()
print(vlans)

# Extend 2 lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

# insert value in a list
list1.insert(3, "INSERT")
print(list1)
list1.insert(0, "BEGIN")
print(list1)

## startwith and endswith methods:
interface_list = [
    "GigabitEthernet0/0",
    "GigabitEthernet0/1",
    "GigabitEthernet0/2",
    "Loopback1",
    "Loopback2",
]
gig_list = []
ends_with_2_list = []
for interface in interface_list:
    if interface.startswith("Giga"):
        gig_list.append(interface)
    if interface.endswith("2"):
        ends_with_2_list.append(interface)

print(gig_list)
print(ends_with_2_list)

## list comprehension to do th same as above
new_gig_list = [i for i in interface_list if i.startswith("Giga")]
print(new_gig_list)

new_gig_list = [i.upper() for i in interface_list if i.startswith("Giga")]
print(new_gig_list)

new_gig_list = ["Soleman" for i in interface_list if i.startswith("Giga")]
print(new_gig_list)

## using filter function
interface_list = [
    "GigabitEthernet0/0",
    "GigabitEthernet0/1",
    "GigabitEthernet0/2",
    "Loopback1",
    "Loopback2",
]
my_gig_list = list(filter(lambda x: x.startswith("Gig"), interface_list))
print(my_gig_list)

## using map function
interface_list = [
    "GigabitEthernet0/0",
    "GigabitEthernet0/1",
    "GigabitEthernet0/2",
    "Loopback1",
    "Loopback2",
]
my_gig_list = list(map(lambda x: x.upper(), interface_list))
print(my_gig_list)
