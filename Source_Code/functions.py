import ipaddress
import tkinter as tk
from ipv4 import *

#Hàm chuyển đổi mã nhị phân
def ipv4_to_binary(address):
    components = map(int, address.split('.'))
    binary_components = [bin(component)[2:].zfill(8) for component in components]
    binary_address = '.'.join(binary_components)

    return binary_address

#kiểm tra phần nhập IP
def check_alphabet(address):
    for char in address:
        if(char.isalpha() == True):
            return False
    return True

def check_ipv4(address):
    try:
        ipaddress.ip_address(address)
        return True
    except ValueError:
        return False
    
#Kiểm tra lớp của địa chỉ IPv4
def check_class(address):
    ipv4_instance = IPv4(address)
    class_ip = int(ipv4_instance.class_ipv4())
    if(0 <= class_ip <= 127):
        return "A"
    elif(128 <= class_ip <= 191):
        return "B"
    elif(192 <= class_ip <= 223):
        return "C"
    
#kiểm tra sự kiện click
def handle_entry(event, action, label, ex):
    if action == "click" and label.get() == ex:
        label.delete(0, tk.END)
        label.config(fg="black", bg="#E9EDF5", font=("Helvetica", 10))
    elif action == "leave" and label.get() == "":
        label.insert(0, ex)
        label.config(fg="grey", bg="white", font=("Helvetica", 10, "italic"))
    else:
        label.config(fg="black", bg="white")

#xử lý hiển thị thông tin kết quả
def info_user_label(frame, info, rows, cols):
    info_label = tk.Label(frame, text=info, font=("Helvetica", 10, "bold"))
    info_label.grid(row=rows, column=cols, sticky="w")
    
#xử lý ẩn hiện frame
def toogle_frame(frame, rows, cols, color):
    if color == "green":
        frame.grid(row=rows, column=cols)
    else:
        frame.grid_forget()