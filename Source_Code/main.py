import sys
import tkinter as tk
from ipv4 import *


def create_main_window():
    app = tk.Tk()
    app.title("CHƯƠNG TRÌNH TÌM CÁC LOẠI ĐỊA CHỈ IP")
    app.geometry("600x400")
    input_ipaddress(app)
    app.mainloop() #chạy chương trình

def input_ipaddress(app):
    global entry
    global error_label
    label = tk.Label(app, text="Nhập địa chỉ IP:")
    label.place(x=0, y=10)

    entry = tk.Entry(app, width=50)
    entry.place(x=90, y=10)

    button = tk.Button(app, text='Xử lý', command= check_input)
    button.place(x=400, y=7)

    error_label = tk.Label(app, text="")
    error_label.place(x=90, y=35)

def check_input():
    user_input = entry.get()
    if '/' in user_input:
        ipaddress, subnet_mask = user_input.split('/')
        if subnet_mask.isdigit():
            if 8 <= int(subnet_mask) < 30:
                error_label.config(text="Địa chỉ IP hợp lệ", fg="green")
            else:
                error_label.config(text="Subnet mask hợp lệ phải nhỏ hơn 30 và lớn hơn hoặc bằng 8", fg="red")
        else:
            error_label.config(text="Bạn chưa nhập subnet mask cho IP", fg="red")
    else:
        error_label.config(text='Bạn chưa nhập subnet mask cho IP', fg="red")

def result_address(app):
    Ipv4 = IPv4(entry.get())
    broadcastip_label = tk.Label(app, text=f"Địa chỉ quảng bá của mạng là: {Ipv4.broadcast()}")
    broadcastip_label.place(x=0, y=50)

    networkip_label = tk.Label(app, text=f"Địa chỉ mạng của mạng là: {Ipv4.network()}")
    networkip_label.place(x=0, y=60)

def main():
    create_main_window()  

if __name__ == '__main__':
    main()
