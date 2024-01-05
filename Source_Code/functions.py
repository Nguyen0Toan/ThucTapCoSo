import ipaddress
import tkinter as tk
from ipv4 import *

#kiểm tra kí tự
def check_alphabet(address):
    for char in address:
        if(char.isalpha() == True):
            return False
    return True

#kiểm tra IPv4
def check_ipv4(address):
    try:
        ip_obj = ipaddress.ip_address(address)
        return isinstance(ip_obj, ipaddress.IPv4Address)
    except ValueError:
        return False
    
#kiểm tra IPv6
def check_ipv6(address):
    try:
        ip_obj = ipaddress.ip_address(address)
        return isinstance(ip_obj, ipaddress.IPv6Address)
    except ValueError:
        return False

#xử lý hiển thị thông tin kết quả
def info_user_label(frame, info, rows, cols):
    info_label = tk.Label(frame, text=info, font=("Helvetica", 10, "bold"))
    info_label.grid(row=rows, column=cols, sticky="w")

#đọc file text như một từ điển
def read_file(file_path):
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            content = file.readlines()
        return content
    except FileNotFoundError:
        return ["Không tìm thấy file"]
    except Exception as e:
        return [f"Có lỗi xảy ra: {str(e)}"]
    
#sự kiện của thanh scrollbar
def on_configure(event, canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

def on_mousewheel_vertical(event, canvas):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

def on_mousewheel_horizontal(event, canvas):
    canvas.xview_scroll(int(-1 * (event.delta / 120)), "units")

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

#xử lý ẩn hiện frame
def toogle_frame(frame, rows, cols, color):
    if color == "green":
        frame.grid(row=rows, column=cols, sticky="nw", padx=20, pady=10)
    else:
        frame.grid_forget()