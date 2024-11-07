import ipaddress

network = ipaddress.ip_network("192.168.10.4/30")
for host in network.hosts():
    print(host)

print("\n",network.netmask)

host1= ipaddress.ip_network("10.0.0.1/30", strict=False)
host2= ipaddress.ip_network("10.0.0.5/30", strict=False)

print(host1, host2)
if host1 == host2:
    print("same subnet")
else:
    print("different subnet")

