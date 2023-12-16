import tkinter as tk
from tkinter import ttk
from ipv4 import *

#font
font_label = ("Helvetica", 10, "bold")
font_normal = ("Helvetica", 10)

def create_main_window():
    app = tk.Tk()
    app.title("CHƯƠNG TRÌNH TÌM CÁC LOẠI ĐỊA CHỈ IP")
    app.geometry("600x400")

    #Frame
    frame = tk.Frame(app)
    frame.pack()

    #user input frame
    user_input_frame = tk.LabelFrame(frame, text="User Input", font=font_label)
    user_input_frame.grid(row=0, column=0)

    #user output frame
    user_output_frame = tk.LabelFrame(frame, text="Result", font=font_label)
    user_output_frame.grid(row=1, column=0)
    
    user_input(user_input_frame)
    user_output(user_output_frame)
    app.mainloop()
    
def user_input(input_frame):
    global input_entry
    global error_label
    global subnet_combobox
    #xử lý nhập dữ liệu của IP
    input_label = tk.Label(input_frame, text="IP Address", font=font_label)
    input_label.grid(row=0, column=0, sticky="w")
    
    input_entry = tk.Entry(input_frame, fg="grey", font=("Helvetica", 10, "italic"))
    input_entry.insert(0, "Example: 192.168.2.3")
    input_entry.bind("<FocusIn>", input_entry_click)
    input_entry.bind('<FocusOut>', input_entry_leave)
    input_entry.grid(row=1, column=0)

    #lựa chọn subnet mask
    subnet_label = tk.Label(input_frame, text="Subnet", font=font_label)
    subnet_label.grid(row=0, column=1, sticky="w")
    
    choices = list(range(1,33))
    subnet_combobox = ttk.Combobox(input_frame, values=choices, width=7, font=font_normal)
    subnet_combobox.grid(row=1, column=1)
    subnet_combobox.set(24)
    
    #xử lý lỗi nhập dữ liệu và phát hiện địa chỉ
    error_label = tk.Label(input_frame, text="", font=font_normal)
    error_label.grid_forget()

    #xử lý dữ liệu bằng button
    handle_button = tk.Button(input_frame, text='Xử lý dữ liệu', font=font_label, command=lambda: check_input(input_entry.get()))
    handle_button.grid(row=3, column=0, columnspan=2, sticky="ew")

    #xử lí padding của các phần tử trong user_input_frame
    for widget in input_frame.winfo_children():
        widget.grid_configure(padx=5, pady=3)
    
#Xử lý sự kiện của input
def input_entry_click(event):
    if input_entry.get() == 'Example: 192.168.2.3':
        input_entry.delete(0,tk.END)
        input_entry.config(fg="black", bg="#E9EDF5", font=font_normal)

def input_entry_leave(event):
    if input_entry.get() == "":
        input_entry.insert(0, "Example: 192.168.2.3")
        input_entry.config(fg="grey", bg="white", font=("Helvetica", 10, "italic"))
    else:
        input_entry.config(fg="black", bg="white")
    
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

#kiểm tra kết quả của input
def check_input(address):
    error_label.grid(row=2, column=0, columnspan=2, sticky="w")
    if(address == "Example: 192.168.2.3"):
        error_label.config(text="Địa chỉ IP không được để trống", fg="red")
    else:
        if(check_alphabet(address) == True):
            if(check_ipv4(address) == True):
                ip_version4 = address
                ipv4_instance = IPv4(address)
                user_output_result(ip_version4)
                if(ipv4_instance.multicast() == True):
                    error_label.config(text="Đây là địa chỉ Multicast", fg="green")
                elif(ipv4_instance.private() == True):
                    error_label.config(text="Đây là địa chỉ Private", fg="green")
                else:
                    error_label.config(text="Địa chỉ hợp lệ", fg="green")
            else:
                error_label.config(text="Địa chỉ IP không hợp lệ xin mời nhập lại", fg="red")
        else:
            error_label.config(text="Không được nhập kí tự xin mời nhập lại", fg="red")

#hiển thị kết quả
def user_output(output_frame):
    #Thông tin của IP
    info_label = tk.Label(output_frame, text="THÔNG TIN CỦA MẠNG", font=("Sonata", 15, "bold"), bg="#013DC4", fg="white")
    info_label.grid(row=0, column=0, columnspan=3, sticky="ew")

    #Hiển thị các loại thông tin của địa chỉ
    #Global các biến
    global address_label, address_binary_label
    global network_label, network_binary_label
    global host_min_label, host_min_binary_label
    global host_max_label, host_max_binary_label
    global broadcast_label, broadcast_binary_label
    global class_result_label, ipv6_result_label

    #IP Address
    info_user_output_label(output_frame, "IP Address:", 1, 0)
    address_label = tk.Label(output_frame, text="", fg="blue", font=("Helvetica", 10))
    address_label.grid(row=1, column=1, sticky="w")

    address_binary_label = tk.Label(output_frame, text="", fg="green", font=("Helvetica, 10"))
    address_binary_label.grid(row=1, column=2)

    #Network
    info_user_output_label(output_frame, "Network:", 2, 0)
    network_label = tk.Label(output_frame, text="", fg="blue", font=("Helvetica", 10))
    network_label.grid(row=2, column=1, sticky="w")

    network_binary_label = tk.Label(output_frame, text="", fg="green", font=("Helvetica, 10"))
    network_binary_label.grid(row=2, column=2)

    #Host Min
    info_user_output_label(output_frame, "Host MIN:", 3, 0)
    host_min_label = tk.Label(output_frame, text="", fg="blue", font=("Helvetica", 10))
    host_min_label.grid(row=3, column=1, sticky="w")

    host_min_binary_label = tk.Label(output_frame, text="", fg="green", font=("Helvetica, 10"))
    host_min_binary_label.grid(row=3, column=2)

    #Host Max
    info_user_output_label(output_frame, "Host MAX", 4, 0)
    host_max_label = tk.Label(output_frame, text="", fg="blue", font=("Helvetica", 10))
    host_max_label.grid(row=4, column=1, sticky="w")

    host_max_binary_label = tk.Label(output_frame, text="", fg="green", font=("Helvetica, 10"))
    host_max_binary_label.grid(row=4, column=2)

    #Broadcast
    info_user_output_label(output_frame, "Broadcast:", 5, 0)
    broadcast_label = tk.Label(output_frame, text="", fg="blue", font=("Helvetica", 10))
    broadcast_label.grid(row=5, column=1, sticky="w")

    broadcast_binary_label = tk.Label(output_frame, text="", fg="green", font=("Helvetica, 10"))
    broadcast_binary_label.grid(row=5, column=2)

    #Class IP
    info_user_output_label(output_frame, "IP Class:", 6, 0)

    class_result_label = tk.Label(output_frame, text="", fg="blue", font=("Helvetica", 10))
    class_result_label.grid(row=6, column=1, sticky="w")

    #IPv6
    info_user_output_label(output_frame, "IPv6:", 7, 0)

    ipv6_result_label = tk.Label(output_frame, text="", fg="blue", font=("Helvetica", 10))
    ipv6_result_label.grid(row=7, column=1, columnspan=2, sticky="ew")

    #xử lí padding của các phần tử trong user_input_frame
    for widget in output_frame.winfo_children():
        widget.grid_configure(padx=3, pady=3)

#xử lý hiển thị thông tin kết quả
def info_user_output_label(output_frame, info, rows, cols):
    #Hiển thị loại thông tin 
    info_label = tk.Label(output_frame, text=info, font=font_label)
    info_label.grid(row=rows, column=cols, sticky="w")

#Xử lý kết quả của dữ liệu
def user_output_result(address):
    #Thông tin các loại IP
    ip = f"{address}/{subnet_combobox.get()}"
    ipv4_instance = IPv4(ip)
    network_ip = ipv4_instance.network()
    broadcast_ip = ipv4_instance.broadcast()
    host_min_ip = ipv4_instance.host_min()
    host_max_ip = ipv4_instance.host_max()
    ipv6 = ipv4_instance.ipv4_to_ipv6()

    #Hiển thị kết quả của dữ liệu
    address_label.config(text=address)
    address_binary_label.config(text=ipv4_to_binary(address))
    
    network_label.config(text=network_ip)
    network_binary_label.config(text=ipv4_to_binary(network_ip))

    host_min_label.config(text=host_min_ip)
    host_min_binary_label.config(text=ipv4_to_binary(host_min_ip))

    host_max_label.config(text=host_max_ip)
    host_max_binary_label.config(text=ipv4_to_binary(host_max_ip))

    broadcast_label.config(text=broadcast_ip)
    broadcast_binary_label.config(text=ipv4_to_binary(broadcast_ip))

    check_class(ip)
    ipv6_result_label.config(text=ipv6)

#Hàm chuyển đổi mã nhị phân
def ipv4_to_binary(address):
    #Chia địa chỉ thành các thành phần 
    components = map(int, address.split('.'))

    #Chuyển đổi địa chỉ sang mã nhị phân
    binary_components = [bin(component)[2:].zfill(8) for component in components]

    #Kết hợp mã nhị phân để tạo địa chỉ IPv4 toàn cục
    binary_address = '.'.join(binary_components)

    return binary_address

#Kiểm tra lớp của địa chỉ IPv4
def check_class(address):
    ipv4_instance = IPv4(address)
    class_ip = int(ipv4_instance.class_ipv4())
    if(0 <= class_ip <= 127):
        class_result_label.config(text="A")
    elif(128 <= class_ip <= 191):
        class_result_label.config(text="B")
    elif(192 <= class_ip <= 223):
        class_result_label.config(text="C")

def main():
    create_main_window()
    
if __name__ == '__main__':
    main()