#!/usr/bin/env python3
import ipaddress

# get ip address 
while True:
    ip4str = input("Enter IPv4 (e.g., 9.254.253.252):")
    try:
        ip4 = ipaddress.IPv4Address(ip4str)
    except ValueError:
        print("invalid ip address. Try, again")
    else:
        break # got ip address

# convert ip4 to rfc 3056 IPv6 6to4 address
# http://tools.ietf.org/html/rfc3056#section-2
prefix6to4 = int(ipaddress.IPv6Address("2002::"))
ip6 = ipaddress.IPv6Address(prefix6to4 | (int(ip4) << 80))
print(ip6)
assert ip6.sixtofour == ip4

# convert ip4 to a base 10
print(int(ip4))
# convert ip4 to binary (0b)
print(bin(int(ip4)))
# convert ip4 to hex (0x)
print(hex(int(ip4)))