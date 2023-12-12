import ipaddress

def ipv4_to_ipv6(ipv4_address):
    ipv4_obj = ipaddress.IPv4Address(ipv4_address)
    ipv6_mapped = ipaddress.IPv6Address(f"::ffff:{ipv4_obj}")
    return str(ipv6_mapped)

# Ví dụ sử dụng:
ipv4_address = "192.0.2.1"
ipv6_address = ipv4_to_ipv6(ipv4_address)
print(f"IPv4: {ipv4_address}")
print(f"IPv6: {ipv6_address}")
