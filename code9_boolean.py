"""These are examples using boolean"""

X = bool(1 + 1 == 2)
print(X, "because 1+1 = 2")

Y = bool(1 + 1 == 3)
print(Y, "because 1+1 != 3")

my_list = []
print(bool(my_list), "beacuse list is empty")

my_list = [1, 2, 3]
print(bool(my_list), "beacuse list is not empty")

Z = None
print(bool(Z), "because is a None value")

print(bool(0), "because is a value of 0")

# if condition using boolean

MY_STR = "hello"

if bool(MY_STR) is True:
    print("string value is True")
if bool(0) is False:
    print("0 is false")

### And, Or, Not operators.
print(bool(1 and 0), "beacuse and")
print(bool(1 or 0), "because or")

## Common mistake using or opperator
## if ROUTING_PROTOCOL == "ospf" or "isis":   >> this is wrong, look at correct below

ROUTING_PROTOCOL = "bgp"

if (
    ROUTING_PROTOCOL == "ospf"
    or ROUTING_PROTOCOL == "isis"
    or ROUTING_PROTOCOL == "bgp"
):
    print(f"routing protocol is {ROUTING_PROTOCOL}")

# easier way to do it:
if ROUTING_PROTOCOL in ["ospf", "isis", "bgp"]:
    print(f"routing protocol is {ROUTING_PROTOCOL}")

if ROUTING_PROTOCOL not in ["ospf", "isis"]:
    print("bgp not in the list")
