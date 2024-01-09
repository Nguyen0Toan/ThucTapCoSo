import ipaddress

class IPv4:
    def __init__(self, address):
        self.address = address
        self.ipv4 = ipaddress.IPv4Interface(address)
        self.ipv6_address = ipaddress.IPv6Address("::ffff:" + str(self.ipv4.network.network_address))

    def network(self):
        ip_parts = list(map(int, str(self.ipv4.ip).split(".")))

        subnet_mask_parts = list(map(int, str(self.ipv4.netmask).split(".")))
            
        network_address_parts = []
        for ip_part, subnet_mask_part in zip(ip_parts, subnet_mask_parts):
            network_address_parts.append(ip_part & subnet_mask_part) 

        network_address = '.'.join(map(str, network_address_parts))
        return network_address
    
    def host_min(self):
        return str(self.ipv4.network.network_address + 1)
    
    def host_max(self):
        return str(self.ipv4.network.broadcast_address - 1)
    
    def broadcast(self):
        network_address = self.network()
    
        network_parts = list(map(int, str(network_address).split('.')))
        
        subnet_mask_parts = list(map(int, str(self.ipv4.netmask).split('.')))

        broadcast_address_parts = []
        for network_part, subnet_mask_part in zip(network_parts, subnet_mask_parts):
            broadcast_address_parts.append(network_part | (255 - subnet_mask_part)) 

        broadcast_address = '.'.join(map(str, broadcast_address_parts))
        return broadcast_address
        
    def multicast(self):
        return self.ipv4.network.is_multicast
    
    def loopback(self):
        if(str(self.ipv4.ip) == "127.0.0.1"):
            return True
        return False
    
    def private(self):
        return self.ipv4.network.is_private
    
    def is_network(self):
        ip_binary = "".join(self.ipv4_to_binary().split("."))
        network_address = ip_binary[self.ipv4.network.prefixlen:]

        for bit in network_address:
            if(int(bit) != 0):
                return False
        return True

    def is_broadcast(self):
        ip_binary = "".join(self.ipv4_to_binary().split("."))
        broadcast_address = ip_binary[self.ipv4.network.prefixlen:]

        for bit in broadcast_address:
            if(int(bit) != 1):
                return False
        return True

    def ipv4_to_binary(self):
        ip_address = str(self.ipv4.ip).split('.')
        ip_binary = []
        for ip in ip_address:
            ip_binary.append(format(int(ip), '08b'))
        return ".".join(ip_binary)
    
    def class_ipv4(self):
        cls_ip = int(self.ipv4.network.network_address.exploded.split(".")[0])
        if(0 <= cls_ip <= 127):
            return "A"
        elif(128 <= cls_ip <= 191):
            return "B"
        elif(192 <= cls_ip <= 223):
            return "C"
        elif(224 <= cls_ip <= 239):
            return "D"
        elif(240 <= cls_ip <= 255):
            return "E"
    
    def ipv4_to_ipv6(self):
        ipv6_format = format(self.ipv6_address, "_X").replace("_", ":")
        return str(ipv6_format)