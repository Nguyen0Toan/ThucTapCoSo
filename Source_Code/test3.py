import ipaddress

def ipv4_to_ipv6(ipv4_address):
    # Tạo một đối tượng IPv6Address từ địa chỉ IPv4
    ipv6_address = ipaddress.IPv6Address("::"+ ipv4_address)
    return ipv6_address

# Nhập địa chỉ IPv4 cần chuyển đổi
ipv4_address = input("Nhập địa chỉ IPv4: ")

# Thực hiện chuyển đổi và in kết quả
ipv6_address = ipv4_to_ipv6(ipv4_address)
formatted_ip = format(ipv6_address, '_X').replace("_",":")

print(formatted_ip)

