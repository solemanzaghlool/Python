class RouterISR4331:

    ## Class Attributes
    vendor = "cisco"
    power = "120W"
    color = "black"
    formfactor = "1U"
    throughput = "100Mbps"
    interfaces = ["gig0", "gig1", "gig2"]

    ##Instance Attributes
    def __init__(self, wic, psu, license):
        self.wic = wic
        self.psu = psu
        self.license = license

    ## Magic Methods / Dunder
    def __len__(self):
        return len(self.interfaces)

    def __contains__(self, interface):
        return interface in self.interfaces

    def __str__(self):
        return f"Router with {self.wic}, {self.psu}, and {self.license} license"

    ## Methods
    def igp(self, protocol):
        if protocol.lower() == "ospf":
            print("router ospf 1\n", " network 10.10.1.1 0.0.0.0 area 0\n")
        elif protocol.lower() == "bgp":
            print("router bgp 65001\n", " network 10.10.1.0 mask 255.255.255.0\n")
        else:
            print("undefined protocol")


r1 = RouterISR4331(wic="NIM-2T", psu="Dual PSU", license="securityk9")

print(r1.color)
print(r1.throughput)
print(r1.wic)
print(r1.igp("ospf"))
print(r1.igp("BGP"))
print(r1.igp("rip"))
print(len(r1))
print(r1.__len__())

if "gig1" in r1:
    print("in list")
else:
    print("not in list")

print(r1)
