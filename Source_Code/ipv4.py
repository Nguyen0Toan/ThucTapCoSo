import ipaddress

class IPv4:
    def __init__(self, address):
        self.address = address
        self.ip = ipaddress.IPv4Network(address, strict=False)

    def broadcast(self):
        return str(self.ip.broadcast_address)
    
    def network(self):
        return str(self.ip.network_address)
    
    def multicast(self):
        return self.ip.is_multicast
    
    def private(self):
        return self.ip.is_private
