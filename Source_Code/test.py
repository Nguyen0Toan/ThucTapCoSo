import ipaddress

class IPv4:
    def __init__(self, address):
        self.address = address
        self.ipv4 = ipaddress.IPv4Network(address, strict=False)

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
        ipv6_format = format(ipaddress.IPv6Address("::" + self.address), '_X').replace('_', ':')
        return str(ipv6_format)

# Sử dụng lớp IPv4
ipv4_instance = IPv4('192.168.0.1/24')

print("Broadcast:", ipv4_instance.broadcast())
print("Network:", ipv4_instance.network())
print("Host Min:", ipv4_instance.host_min())
print("Host Max:", ipv4_instance.host_max())
print("Class IPv4:", ipv4_instance.class_ipv4())
print("Is Multicast:", ipv4_instance.multicast())
print("Is Private:", ipv4_instance.private())
print("IPv4 to IPv6:", ipv4_instance.ipv4_to_ipv6())
