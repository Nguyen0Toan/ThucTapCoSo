import ipaddress

network = ipaddress.IPv4Network("192.168.1.0/24")
print("Network Address:", network.network_address)
print("Broadcast Address:", network.broadcast_address)
print("Number of Addresses:", (network.num_addresses) - 2)
print("Prefix Length:", network.prefixlen)
subnet_mask = ipaddress.IPv4Network(f"0.0.0.0/{network.prefixlen}", strict=False).network_address
print("Network Mask:", subnet_mask)
print("Hosts:")
for ip in network.hosts():
    print(ip)