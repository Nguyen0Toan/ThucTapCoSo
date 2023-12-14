def ipv4_to_binary(address):
    #Chia địa chỉ thành các thành phần 
    components = map(int, address.split('.'))

    #Chuyển đổi địa chỉ sang mã nhị phân
    binary_components = [bin(component)[2:].zfill(8) for component in components]

    #Kết hợp mã nhị phân để tạo địa chỉ IPv4 toàn cục
    binary_address = '.'.join(binary_components)

    return binary_address

print(ipv4_to_binary("192.168.2.3"))