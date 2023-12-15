import ipaddress

ip = ipaddress.IPv4Address("192.168.1.1")
exploded_ip = ip.split(".")[0]

print(exploded_ip)
# Output: '192.168.1.1'
