"""These are examples of manipulating Dics"""

devices = {"host1": "10.1.1.1", "host2": "10.1.1.2", "host3": "10.1.1.3"}

print(devices)
print("\n")

print(devices["host2"])

# Adding new entry to dictionary
devices["host4"] = "10.1.1.4"
devices["host5"] = "10.1.1.5"
print(devices)
print("\n")

# Get list of keys, and values
devices_keys = devices.keys()
print(list(devices_keys))

devices_values = devices.values()
print(list(devices_values))

## list of dictionaries
people = [
    {"name": "Soleman", "age": 20, "job": "engineer"},
    {"name": "Nora", "age": 21, "job": "doctor"},
]

print(people)
print(people[0])
print(people[0]["name"])
print(people[1]["job"])

# get value from dictionary, or print it cannot be found if it doesn't exist
x = people[0].get("age", "This key can't be found")
print(x)
x = people[0].get("hobbies", "This key can't be found")
print(x)

# delete key/value pair
print(devices)
del devices["host5"]
print(devices)

# pop key and return it to a seperate variable
popped_key = devices.pop("host1")
print(devices)
print(popped_key)

x = devices.pop("host6", "Key doesn't exist")
print(x)

# get key/value pairs in a list of tuples
print(devices)
print(list(devices.items()))

# for loop using k/v:
for key in devices.keys():
    print(key)
print("\n")

for value in devices.values():
    print(value)

for k, v in devices.items():
    print(f"the value of {k} is {v}")

## unpacking dictionary

devices1 = {"host1": "10.1.1.1", "host2": "10.1.1.2", "host3": "10.1.1.3"}

devices2 = {"host4": "10.1.1.4", "host5": "10.1.1.5", "host6": "10.1.1.6"}

total_devices = {**devices1, **devices2}
print(total_devices)

# Dictionary comprehensions
ages = {"Soleman": 22, "Mike": 44, "Nora": 20}
new_ages = {k: v for (k, v) in ages.items() if v > 20}
print(new_ages)
