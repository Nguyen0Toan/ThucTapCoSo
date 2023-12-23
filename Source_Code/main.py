import tkinter as tk
from tkinter import ttk
import functions as func
from ipv4 import *

#font
font_label = ("Helvetica", 10, "bold")
font_normal = ("Helvetica", 10)

#tạo chương trình cửa sổ
def create_main_window():
    app = tk.Tk()
    app.title("CHƯƠNG TRÌNH TÌM CÁC LOẠI ĐỊA CHỈ IP")
    app.geometry("600x400")

    #frame
    main_frame = tk.Frame(app)
    main_frame.pack(fill=tk.BOTH, expand=1)

    canvas = tk.Canvas(main_frame)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.LEFT, fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    second_frame = tk.Frame(canvas)

    canvas.create_window((50,10), window=second_frame, anchor="nw")

    #ipv4 input frame
    ipv4_input_frame = tk.LabelFrame(second_frame, text="IPv4 Input", font=font_label)
    ipv4_input_frame.grid(row=0, column=0)

    #ipv6 input frame
    ipv6_input_frame = tk.LabelFrame(second_frame, text="IPv6 Input", font=font_label)
    ipv6_input_frame.grid(row=1, column=0)

    #ipv4 and subnet output frame
    global ipv4_output_frame
    global subnet_output_frame
    ipv4_output_frame = tk.LabelFrame(second_frame, text="IPv4 Result", font=font_label)

    subnet_output_frame = tk.LabelFrame(second_frame, text="IPv4 Subnetting", font=font_label)
    
    ipv4_input(ipv4_input_frame)
    ipv6_input(ipv6_input_frame)
    user_output(ipv4_output_frame)
    subnetting_output(subnet_output_frame)

    app.mainloop()

#xử lý nhập của ipv4
def ipv4_input(ipv4_frame):
    global error_label
    global subnet_combobox
    example = "Example: 192.168.2.3"
    #xử lý nhập dữ liệu của IP
    func.info_user_label(ipv4_frame, "IPv4 Address", 0, 0)
    
    input_entry = tk.Entry(ipv4_frame, fg="grey", font=("Helvetica", 10, "italic"), width=40)
    input_entry.insert(0, example)
    input_entry.bind("<FocusIn>", lambda event: func.handle_entry(event, "click", input_entry, example))
    input_entry.bind('<FocusOut>', lambda event: func.handle_entry(event, "leave", input_entry, example))
    input_entry.grid(row=1, column=0)

    #lựa chọn subnet mask
    func.info_user_label(ipv4_frame, "Subnet", 0, 1)
    
    choices = list(range(1,33))
    subnet_combobox = ttk.Combobox(ipv4_frame, values=choices, width=7, font=font_normal)
    subnet_combobox.grid(row=1, column=1)
    subnet_combobox.set(24)
    
    #xử lý lỗi nhập dữ liệu và phát hiện địa chỉ
    error_label = tk.Label(ipv4_frame, text="", font=font_normal)

    #xử lý dữ liệu bằng button
    handle_button = tk.Button(ipv4_frame, text='Xử lý dữ liệu', font=font_label, command=lambda: check_input(input_entry.get()))
    handle_button.grid(row=3, column=0, columnspan=2, sticky="ew")

    #xử lí padding của các phần tử trong ipv4_input_frame
    for widget in ipv4_frame.winfo_children():
        widget.grid_configure(padx=5, pady=3)

#xử lý nhập của ipv6
def ipv6_input(ipv6_frame):
    example = "Example: 2001:db8:85a3::8a2e:370:7334"
    func.info_user_label(ipv6_frame, "IPv6 Address", 0, 0)

    input_entry = tk.Entry(ipv6_frame, fg="grey", font=("Helvetica", 10, "italic"), width=37)
    input_entry.insert(0, example)
    input_entry.bind("<FocusIn>", lambda event: func.handle_entry(event, "click", input_entry, example))
    input_entry.bind('<FocusOut>', lambda event: func.handle_entry(event, "leave", input_entry, example))
    input_entry.grid(row=1, column=0)

    #lựa chọn subnet mask
    func.info_user_label(ipv6_frame, "Prefix Length", 0, 1)
    
    choices = list(range(1,129))
    prefix_length_combobox = ttk.Combobox(ipv6_frame, values=choices, width=7, font=font_normal)
    prefix_length_combobox.grid(row=1, column=1, sticky="w")
    prefix_length_combobox.set(64)
    
    #xử lý lỗi nhập dữ liệu và phát hiện địa chỉ
    error_label = tk.Label(ipv6_frame, text="", font=font_normal)

    #xử lý dữ liệu bằng button
    handle_button = tk.Button(ipv6_frame, text='Xử lý dữ liệu', font=font_label, command=lambda: check_input(input_entry.get()))
    handle_button.grid(row=3, column=0, columnspan=2, sticky="ew")

    #xử lí padding của các phần tử trong ipv4_input_frame
    for widget in ipv6_frame.winfo_children():
        widget.grid_configure(padx=5, pady=3)

#kiểm tra kết quả của ipv4
def check_input(address):
    error_label.grid(row=2, column=0, columnspan=2, sticky="w")
    if(address == "Example: 192.168.2.3"):
        error_label.config(text="Địa chỉ IP không được để trống", fg="red")
    else:
        if(func.check_alphabet(address) == True):
            if(func.check_ipv4(address) == True):
                ip_version4 = f"{address}/{subnet_combobox.get()}"
                ipv4_instance = IPv4(ip_version4)
                user_output_result(ip_version4)
                subnetting_output_result(ip_version4)
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

    color = error_label.cget("foreground")
    if(color == "green"):
        func.toogle_frame(ipv4_output_frame, 2, 0, color)
        func.toogle_frame(subnet_output_frame, 3, 0, color)
    else:
        func.toogle_frame(ipv4_output_frame, color)
        func.toogle_frame(subnet_output_frame, color)

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
    func.info_user_label(output_frame, "IP Address:", 1, 0)
    address_label = tk.Label(output_frame, text="", fg="blue", font=font_normal)
    address_label.grid(row=1, column=1, sticky="w")

    address_binary_label = tk.Label(output_frame, text="", fg="green", font=font_normal)
    address_binary_label.grid(row=1, column=2)

    #Network
    func.info_user_label(output_frame, "Network:", 2, 0)
    network_label = tk.Label(output_frame, text="", fg="blue", font=font_normal)
    network_label.grid(row=2, column=1, sticky="w")

    network_binary_label = tk.Label(output_frame, text="", fg="green", font=font_normal)
    network_binary_label.grid(row=2, column=2)

    #Host Min
    func.info_user_label(output_frame, "Host MIN:", 3, 0)
    host_min_label = tk.Label(output_frame, text="", fg="blue", font=font_normal)
    host_min_label.grid(row=3, column=1, sticky="w")

    host_min_binary_label = tk.Label(output_frame, text="", fg="green", font=font_normal)
    host_min_binary_label.grid(row=3, column=2)

    #Host Max
    func.info_user_label(output_frame, "Host MAX", 4, 0)
    host_max_label = tk.Label(output_frame, text="", fg="blue", font=font_normal)
    host_max_label.grid(row=4, column=1, sticky="w")

    host_max_binary_label = tk.Label(output_frame, text="", fg="green", font=font_normal)
    host_max_binary_label.grid(row=4, column=2)

    #Broadcast
    func.info_user_label(output_frame, "Broadcast:", 5, 0)
    broadcast_label = tk.Label(output_frame, text="", fg="blue", font=font_normal)
    broadcast_label.grid(row=5, column=1, sticky="w")

    broadcast_binary_label = tk.Label(output_frame, text="", fg="green", font=font_normal)
    broadcast_binary_label.grid(row=5, column=2)

    #Class IP
    func.info_user_label(output_frame, "IP Class:", 6, 0)

    class_result_label = tk.Label(output_frame, text="", fg="blue", font=font_normal)
    class_result_label.grid(row=6, column=1, sticky="w")

    #IPv6
    func.info_user_label(output_frame, "IPv4 mapped IPv6:", 7, 0)

    ipv6_result_label = tk.Label(output_frame, text="", fg="blue", font=font_normal)
    ipv6_result_label.grid(row=7, column=1, columnspan=2, sticky="ew")

    #xử lí padding của các phần tử trong ipv4_input_frame
    for widget in output_frame.winfo_children():
        widget.grid_configure(padx=3, pady=3)

#xử lý kết quả của dữ liệu
def user_output_result(address):
    #Thông tin các loại IP
    ipv4_instance = IPv4(address)
    ipv4 = address.split("/")[0]
    network_ip = ipv4_instance.network()
    broadcast_ip = ipv4_instance.broadcast()
    host_min_ip = ipv4_instance.host_min()
    host_max_ip = ipv4_instance.host_max()
    ipv6 = ipv4_instance.ipv4_to_ipv6()

    #Hiển thị kết quả của dữ liệu
    address_label.config(text=address)
    address_binary_label.config(text=func.ipv4_to_binary(ipv4))
    
    network_label.config(text=network_ip)
    network_binary_label.config(text=func.ipv4_to_binary(network_ip))

    host_min_label.config(text=host_min_ip)
    host_min_binary_label.config(text=func.ipv4_to_binary(host_min_ip))

    host_max_label.config(text=host_max_ip)
    host_max_binary_label.config(text=func.ipv4_to_binary(host_max_ip))

    broadcast_label.config(text=broadcast_ip)
    broadcast_binary_label.config(text=func.ipv4_to_binary(broadcast_ip))

    class_result_label.config(text=func.check_class(ipv4))
    
    ipv6_result_label.config(text=ipv6)

#subnetting
def subnetting_output(subnet_frame):
    title_label = tk.Label(subnet_frame, text="SUBNETTING", font=("Sonata", 15, "bold"), bg="#013DC4", fg="white")
    title_label.grid(row=0, column=0, columnspan=3, sticky="ew")

    func.info_user_label(subnet_frame, "Network", 1, 0)
    func.info_user_label(subnet_frame, "Host min - Host max", 1, 1)
    func.info_user_label(subnet_frame, "Broadcast", 1, 2)

    #xử lí padding của các phần tử trong subnetting
    for widget in subnet_frame.winfo_children():
        widget.grid_configure(padx=24, pady=3)

#hiển thị kết quả của subnetting
def subnetting_output_result(address):
    ipv4_instance = IPv4(address)
    subnets = ipv4_instance.subnetting()

    for subnet in subnets:
        ipv4_subnet = IPv4(subnet)
        network_ip = ipv4_subnet.network()
        broadcast_ip = ipv4_subnet.broadcast()
        host_min_ip = ipv4_subnet.host_min()
        host_max_ip = ipv4_subnet.host_max()

        func.info_user_label(subnet_output_frame, network_ip, 2, 0)
        func.info_user_label(subnet_output_frame, f"{host_min_ip} - {host_max_ip}", 2, 1)
        func.info_user_label(subnet_output_frame, broadcast_ip, 2, 2)

def main():
    create_main_window()
    
if __name__ == '__main__':
    main()