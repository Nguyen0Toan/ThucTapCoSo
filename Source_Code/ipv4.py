import ipaddress

class IPv4:
    def __init__(self, address):
        self.address = address
        self.ipv4 = ipaddress.IPv4Network(address, strict=False)
        self.ipv6_address = ipaddress.IPv6Address("::ffff:" + str(self.ipv4.network_address))

    def network(self):
        return str(self.ipv4.network_address)
    
    def host_min(self):
        return str(self.ipv4.network_address + 1)
    
    def host_max(self):
        return str(self.ipv4.broadcast_address - 1)
    
    def broadcast(self):
        return str(self.ipv4.broadcast_address)
    
    def class_ipv4(self):
        cls_ip = int(self.ipv4.network_address.exploded.split(".")[0])
        if(0 <= cls_ip <= 127):
            return "A"
        elif(128 <= cls_ip <= 191):
            return "B"
        elif(192 <= cls_ip <= 223):
            return "C"
        
    def multicast(self):
        return self.ipv4.is_multicast
    
    def private(self):
        return self.ipv4.is_private
    
    def ipv4_to_ipv6(self):
        ipv6_format = format(self.ipv6_address, "_X").replace("_", ":")
        return str(ipv6_format)
    
