import ipaddress

def subnet_list(base_ip, subnet_prefix):
    base_network = ipaddress.IPv4Network(f"{base_ip}/{subnet_prefix}", strict=False)
    subnets = list(base_network.subnets(new_prefix=20))
    return subnets

# Địa chỉ IP cơ sở và độ dài tiền tố của subnet
base_ip = "192.168.2.3"
subnet_prefix = 16

# Lấy danh sách tất cả các subnet
subnets = subnet_list(base_ip, subnet_prefix)

# Hiển thị tất cả các subnet
for subnet in subnets:
    print(subnet)
