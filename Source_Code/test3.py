import ipaddress

def is_valid_ip_address(ip_string):
    try:
        ipaddress.ip_address(ip_string)
        return True
    except ValueError:
        return False

# Sử dụng hàm kiểm tra
user_input = "192.168.1.1"
if is_valid_ip_address(user_input):
    print("Đây là địa chỉ IP hợp lệ.")
else:
    print("Đây không phải là địa chỉ IP hợp lệ.")
