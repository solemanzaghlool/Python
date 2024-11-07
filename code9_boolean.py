"""These are examples using boolean"""

x = bool(1+1 == 2)
print(x, "because 1+1 = 2")

y = bool(1+1 == 3)
print(y, "because 1+1 != 3")

my_list = []
print (bool(my_list), "beacuse list is empty")

my_list = [1,2,3]
print (bool(my_list), "beacuse list is not empty")

z = None
print (bool(z), "because is a None value")

print (bool(0), "because is a value of 0")

#if condition using boolean

my_str = "hello"

if bool(my_str) == True:
    print("string value is True")
if bool(0) == False:
    print("0 is false")

### And, Or, Not operators.
print(bool(1 and 0), "beacuse and")
print(bool(1 or 0), "because or")

## Common mistake using or opperator
## if routing_protocol == "ospf" or "isis":   >> this is wrong, look at correct below

routing_protocol = "bgp"

if routing_protocol =="ospf" or routing_protocol == "isis" or routing_protocol == "bgp":
     print(f"routing protocol is {routing_protocol}")

#easier way to do it:
if routing_protocol in ["ospf", "isis", "bgp"]:
    print(f"routing protocol is {routing_protocol}")

if routing_protocol not in ["ospf", "isis"]:
    print("bgp not in the list")
