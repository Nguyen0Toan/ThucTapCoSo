from ipwhois import IPWhois
import ipaddress

def get_ip_type(ip_address):
    try:
        # Kiểm tra xem địa chỉ IP có phải là địa chỉ public hay không
        ip_type = IPWhois(ip_address).lookup_rdap()['asn']
        return f"Địa chỉ IP {ip_address} là địa chỉ public (ASN: {ip_type})"
    except Exception as e:
        return f"Địa chỉ IP {ip_address} là địa chỉ private: {str(e)}"

# Nhập địa chỉ IPv4 cần kiểm tra
ipv4_address = input("Nhập địa chỉ IPv4: ")

# Kiểm tra và in kết quả
result = get_ip_type(ipv4_address)
print(result)
