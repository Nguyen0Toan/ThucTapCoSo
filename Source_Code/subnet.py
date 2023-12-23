import ipaddress

class subnet:
    def __init__(self, address):
        self.address = address
        self.ip = ipaddress.IPv4Address(address, strict=False)

    def network(self):
        return str(self.ip.network_address)
    
    def broadcast(self):
        return str(self.ip.broadcast_address)
    
    def host_min(self):
        return str(self.ip.network_address + 1)
    
    def host_max(self):
        return str(self.ip.broadcast_address - 1)