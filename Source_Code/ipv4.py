import ipaddress

class IPv4:
    def __init__(self, address):
        self.address = address
        self.ipv4 = ipaddress.IPv4Network(address, strict=False)
        self.ip = str(self.ipv4.network_address)
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
    
    def subnetting(self):
        subnet_prefix = 1
        subnetmask = int(self.ipv4.prefixlen)
        if 8 <= subnetmask < 16:
            subnet_prefix = 8
        elif 16 <= subnetmask < 24:
            subnet_prefix = 16

        base_network = ipaddress.IPv4Network(f"{self.ip}/{subnet_prefix}", strict=False)
        subnets = list(base_network.subnets(new_prefix=subnetmask))
        return subnets
