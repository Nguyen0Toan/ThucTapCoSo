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
    
    def unicast(self):
        return all(
            not getattr(self.ipv6.ip, f"is_{attr}")()
            for attr in ["multicast", "unspecified", "loopback", "link_local", "site_local", "sitelocal", "multicast", "reserved"]
        )
    
    def anycast(self):
        return self.ipv6.ip.is_multicast and not self.ipv6.ip.is_reserved
    
    def ipv6_to_binary(self):
        binary_ipv6 = bin(int(self.ipv6))[2:]
        binary_with_dot = ".".join([binary_ipv6.zfill(128)[i:i+16] for i in range(0, 128, 16)])
        return binary_with_dot