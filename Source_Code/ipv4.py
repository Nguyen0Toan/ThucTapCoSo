import ipaddress

class IPv4:
    def __init__(self, address):
        self.address = address
        self.network_ip = ipaddress.IPv4Network(address, strict=False)

    def broadcast(self):
        return str(self.network_ip.broadcast_address)
    
    def network(self):
        return str(self.network_ip.network_address)
    
    def multicast(self):
        return self.network_ip.is_multicast