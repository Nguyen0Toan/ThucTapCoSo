import sys
from ipv4 import *

def main():
    address = input('Nhập địa chỉ IP của bạn: ')

    available_subnet_mask = address.split('/')
    if(int(available_subnet_mask[1]) < 30):
        IPV4 = IPv4(address)
        print(IPV4.broadcast())
    else:
        sys.exit('Subnet mask không đủ để tìm địa chỉ quảng bá và địa chỉ mạng')   

if __name__ == '__main__':
    main()
