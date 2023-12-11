import ipaddress

class IPv4:
    def __init__(self, address):
        self.address = address
        self.network = ipaddress.IPv4Network(address, strict=False)

    def broadcast(self):
        return str(self.network.broadcast_address)
    
    def network(self):
        return str(self.network.network_address)