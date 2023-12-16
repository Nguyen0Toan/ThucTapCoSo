import ipaddress

class IPv4:
    def __init__(self, address):
        self.address = address
        self.ipv4 = ipaddress.IPv4Network(address, strict=False)
        self.ipv6 = ipaddress.IPv6Address("::" + str(self.ipv4.network_address))

    def broadcast(self):
        return str(self.ipv4.broadcast_address)
    
    def network(self):
        return str(self.ipv4.network_address)
    
    def host_min(self):
        return str(self.ipv4.network_address + 1)
    
    def host_max(self):
        return str(self.ipv4.broadcast_address - 1)
    
    def class_ipv4(self):
        return self.ipv4.network_address.exploded.split(".")[0]
        
    def multicast(self):
        return self.ipv4.is_multicast
    
    def private(self):
        return self.ipv4.is_private
    
    def ipv4_to_ipv6(self):
        ipv6_format = format(self.ipv6, "_X").replace("_", ":")
        return str(ipv6_format)
    
