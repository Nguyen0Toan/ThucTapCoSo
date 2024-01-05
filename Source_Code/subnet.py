import ipaddress
from ipv4 import IPv4

class Subnet(IPv4):
    def __init__(self, address):
        super().__init__(address)

    def network(self):
        return super().network()
    
    def host_min(self):
        return super().host_min()
    
    def host_max(self):
        return super().host_max()
    
    def broadcast(self):
        return super().broadcast()
    
    def subnetting(self):
        subnet_prefix = 1
        subnetmask = int(self.ipv4.network.prefixlen)
        if 8 <= subnetmask < 16:
            subnet_prefix = 8
        elif 16 <= subnetmask < 24:
            subnet_prefix = 16
        elif 24 <= subnetmask < 32:
            subnet_prefix = 24
        base_network = ipaddress.IPv4Network(f"{self.ipv4.network.network_address}/{subnet_prefix}", strict=False)
        subnets = list(base_network.subnets(new_prefix=subnetmask))
        return subnets