"""These are examples of using the if condition statements"""

## Example using math operators and 'and' logic
age  = input("Please your age: ")
age = int(age)

if age > 20:
    print("You are older than 20")
elif age <= 20 and age > 10:
    print("Your age is between 10 and 20")
else:
    print("You are a child")


## Example checking if a value is in a list or dict

my_list = ["R1", "R2", "R3"]
my_dict = {"host1":"R1","host2":"R2"}
my_string = "R1"


if my_string in my_list:
    print("valid list")

if "host1" in my_dict:
    print("valid dict")

if my_string in my_dict.values():
    print("valid dict2")


## boolean

routing_protocol = "bgp"

if routing_protocol =="ospf" or routing_protocol == "isis" or routing_protocol == "bgp":
     print(f"routing protocol is {routing_protocol}")

#easier way to do it:
if routing_protocol in ["ospf", "isis", "bgp"]:
    print(f"routing protocol is {routing_protocol}")

if routing_protocol not in ["ospf", "isis"]:
    print("bgp not in the list")

