import ipaddress

class IPv6:
    def __init__(self, address):
        self.ipv6 = ipaddress.IPv6Interface(address)

    def network(self):
        return str(self.ipv6.network.network_address)
    
    def full_ipv6(self):
        return str(self.ipv6.ip.exploded)
    
    def multicast(self):
        return self.ipv6.ip.is_multicast