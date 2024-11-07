"""These are examples of manipulating Sets"""

# Print set with no particular order and REMOVES duplicates
my_set = {"Monday", "Tuesday", "Wednesday", "Monday", "Wednesday"}
print(my_set)

# Add an entry to the set
my_set.add("Friday")
print(my_set)

# Remove an entry to the set
my_set.remove("Monday")
print(my_set)

##operations with sets
ip_adds1 = {"192.168.4.1", "192.168.4.2", "192.168.4.3"}
ip_adds2 = {"192.168.4.3", "192.168.4.4", "192.168.4.5"}

adds1_diff = ip_adds1 - ip_adds2
adds2_diff = ip_adds2 - ip_adds1
print(adds1_diff)
print(adds2_diff)

print(ip_adds1.intersection(ip_adds2))
print(ip_adds1.union(ip_adds2))
