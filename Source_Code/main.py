import tkinter as tk
from tkinter import ttk
import functions as func
import webbrowser
from ipv4 import *
from ipv6 import *
from subnet import *

#font
font_label = ("Helvetica", 10, "bold")
font_normal = ("Helvetica", 10)

#frame tạo chương trình với thanh lăn chuột
def scrollbar_window(app):
    main_frame = tk.Frame(app)
    main_frame.pack(fill=tk.BOTH, expand=1)

    canvas = tk.Canvas(main_frame)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.LEFT, fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    second_frame = tk.Frame(canvas)
    second_frame.pack(expand="true", fill="both")

    canvas.create_window((10,10), window=second_frame, anchor="nw")
    main_window(second_frame)
    
#frame chính chứa toàn bộ nội dung chương trình
def main_window(main_frame):
    global ipv4_output_frame, ipv6_output_frame
    global subnetting_output_frame
    global sup_subnetting_frame, main_subnetting_frame

    #documents frame
    documents_frame = tk.LabelFrame(main_frame, text="Tài Liệu Tham Khảo", font=font_label, bg="#008170", fg="white")
    documents_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")

    #ipv4 input, output frame
    ipv4_input_frame = tk.LabelFrame(main_frame, text="IPv4 Input", font=font_label, )
    ipv4_input_frame.grid(row=0, column=1, sticky="nw")

    ipv4_output_frame = tk.LabelFrame(main_frame, text="IPv4 Result", font=font_label)
    subnetting_output_frame = tk.LabelFrame(main_frame, text="IPv4 Subnetting", font=font_label)
    main_subnetting_frame = tk.Frame(subnetting_output_frame)
    main_subnetting_frame.grid(row=0, column=0)
    sup_subnetting_frame = tk.Frame(subnetting_output_frame)
    sup_subnetting_frame.grid(row=1, column=0)


    #ipv6 input, output frame
    ipv6_input_frame = tk.LabelFrame(main_frame, text="IPv6 Input", font=font_label)
    ipv6_input_frame.grid(row=1, column=1, sticky="nw")
    ipv6_output_frame  = tk.LabelFrame(main_frame, text="IPv6 Result", font=font_label)
    
    for widget in main_frame.winfo_children():
        widget.grid_configure(padx=20, pady=10)

    ipv4_output_frame.grid_forget()
    ipv6_output_frame.grid_forget()
    subnetting_output_frame.grid_forget()

    documents(documents_frame)
    ipv4_input(ipv4_input_frame)
    ipv6_input(ipv6_input_frame)
    ipv4_output(ipv4_output_frame)
    ipv6_output(ipv6_output_frame)
    subnetting_output(main_subnetting_frame)

#xử lý tài liệu tham khảo
def documents(document_frame):
    global links
    global link_listbox
    links={
        "Internet Protocol version 4(IPv4)": "https://en.wikipedia.org/wiki/Internet_Protocol_version_4",
        "Broadcast Address": "https://en.wikipedia.org/wiki/Broadcast_address",
        "Network Address": "https://en.wikipedia.org/wiki/Network_address",
        "Multicast Address": "https://en.wikipedia.org/wiki/Multicast_address",
        "Internet Protocol version 6(IPv6)": "https://en.wikipedia.org/wiki/IPv6",
        "Subnet": "https://en.wikipedia.org/wiki/Subnet",
        "Classful network": "https://en.wikipedia.org/wiki/Classful_network",
        "Private network": "https://en.wikipedia.org/wiki/Private_network",
    }

    link_listbox = tk.Listbox(document_frame, selectmode=tk.SINGLE, font=font_normal, fg="blue", width=30)
    link_listbox.grid(row=0, column=0, sticky="nw")
    for link in links:
        link_listbox.insert(tk.END, link)

    link_listbox.bind("<<ListboxSelect>>", show_documentation)
    document_frame.configure(padx=10, pady=10)
    document_frame.bind("<Configure>", lambda event, lb=link_listbox: on_frame_resize(event, lb))

#sự kiện đường dẫn đến tài liệu
def show_documentation(event):
    selected_index = link_listbox.curselection()
    if selected_index:
        selected_index = int(selected_index[0])
        selected_link = list(links.values())[selected_index]
        webbrowser.open(selected_link)

def on_frame_resize(event, listbox):
    new_height = event.height  
    new_listbox_height = new_height - 20  
    listbox.config(height=int(new_listbox_height / 20))

#xử lý nhập của ipv4
def ipv4_input(ipv4_frame):
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
    error_ipv4_label = tk.Label(ipv4_frame, text="", font=font_normal)

    #xử lý dữ liệu bằng button
    handle_button = tk.Button(ipv4_frame, text='Xử lý dữ liệu', font=font_label, command=lambda: check_input_ipv4(input_entry.get(), error_ipv4_label, example, subnet_combobox.get()))
    handle_button.grid(row=3, column=0, columnspan=2, sticky="ew")

    #xử lí padding của các phần tử trong ipv4_input_frame
    for widget in ipv4_frame.winfo_children():
        widget.grid_configure(padx=5, pady=3)

    error_ipv4_label.grid_forget()

#kiểm tra kết quả của ipv4
def check_input_ipv4(address, label, example, combo):
    label.grid(row=2, column=0, columnspan=2, sticky="w")
    label.grid_configure(padx=5, pady=3)

    if(address == example):
        label.config(text="Địa chỉ IP không được để trống", fg="red")
    else:
        if(func.check_alphabet(address) == True):
            if(func.check_ipv4(address) == True):
                ipv4_instance = IPv4(address)
                ipv4_output_result(address, combo)
                subnetting_output_result(address, combo)
                if(ipv4_instance.multicast() == True):
                    label.config(text="Đây là địa chỉ Multicast", fg="green")
                elif(ipv4_instance.private() == True):
                    label.config(text="Đây là địa chỉ Private", fg="green")
                else:
                    label.config(text="Địa chỉ hợp lệ", fg="green")
            else:
                label.config(text="Địa chỉ IP không hợp lệ xin mời nhập lại", fg="red")
        else:
            label.config(text="Không được nhập kí tự xin mời nhập lại", fg="red")

    color = label.cget("foreground")
    func.toogle_frame(ipv4_output_frame, 2, 1, color)
    func.toogle_frame(subnetting_output_frame, 3, 1, color)
    ipv6_output_frame.grid_forget()

#xử lý nhập của ipv6
def ipv6_input(ipv6_frame):
    example = "Example: 2001:db8:85a3::8a2e:370:7334"
    #phần nhập của IPv6
    func.info_user_label(ipv6_frame, "IPv6 Address", 0, 0)
    input_ipv6_entry = tk.Entry(ipv6_frame, fg="grey", font=("Helvetica", 10, "italic"), width=37)
    input_ipv6_entry.insert(0, example)
    input_ipv6_entry.bind("<FocusIn>", lambda event: func.handle_entry(event, "click", input_ipv6_entry, example))
    input_ipv6_entry.bind('<FocusOut>', lambda event: func.handle_entry(event, "leave", input_ipv6_entry, example))
    input_ipv6_entry.grid(row=1, column=0)

    #lựa chọn subnet mask
    func.info_user_label(ipv6_frame, "Prefix Length", 0, 1)
    choices = list(range(1,129))
    prefix_length_combobox = ttk.Combobox(ipv6_frame, values=choices, width=7, font=font_normal)
    prefix_length_combobox.grid(row=1, column=1, sticky="w")
    prefix_length_combobox.set(64)
    
    #xử lý lỗi nhập dữ liệu và phát hiện địa chỉ
    error_ipv6_label = tk.Label(ipv6_frame, text="", font=font_normal)

    #xử lý dữ liệu bằng button
    handle_button = tk.Button(ipv6_frame, text='Xử lý dữ liệu', font=font_label, command=lambda: check_input_ipv6(input_ipv6_entry.get(), error_ipv6_label, example, prefix_length_combobox.get()))
    handle_button.grid(row=3, column=0, columnspan=2, sticky="ew")

    #xử lí padding của các phần tử trong ipv4_input_frame
    for widget in ipv6_frame.winfo_children():
        widget.grid_configure(padx=5, pady=3)

    error_ipv6_label.grid_forget()

#kiểm tra kết quả của ipv6
def check_input_ipv6(address, label, example, combo):
    label.grid(row=2, column=0, columnspan=2, sticky="w")
    label.grid_configure(padx=5, pady=3)

    if(address == example):
        label.config(text="Địa chỉ IP không được để trống", fg="red")
    else:
        if(func.check_ipv6(address) == True):
            ipv6_instance = IPv6(f"{address}/{combo}")
            ipv6_ouput_result(address, combo)
            if(ipv6_instance.multicast()):
                label.config("Đây là địa chỉ Multicast", fg="green")
            else:
                label.config(text="Địa chỉ hợp lệ", fg="green")
        else:
            label.config(text="Địa chỉ IP không hợp lệ xin mời nhập lại", fg="red")

    color = label.cget("foreground")
    func.toogle_frame(ipv6_output_frame, 2, 1, color)
    ipv4_output_frame.grid_forget()
    subnetting_output_frame.grid_forget()

#hiển thị kết quả
def ipv4_output(output_frame):
    #Global các biến
    global address_label, address_binary_label
    global network_label, network_binary_label
    global host_min_label, host_min_binary_label
    global host_max_label, host_max_binary_label
    global broadcast_label, broadcast_binary_label
    global class_result_label, ipv6_result_label

    #Thông tin của IP
    info_label = tk.Label(output_frame, text="THÔNG TIN CỦA MẠNG", font=("Sonata", 15, "bold"), bg="#013DC4", fg="white")
    info_label.grid(row=0, column=0, columnspan=3, sticky="ew")

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
    ipv6_result_label.grid(row=7, column=1, columnspan=2, sticky="w")

    #xử lí padding của các phần tử trong ipv4_input_frame
    for widget in output_frame.winfo_children():
        widget.grid_configure(padx=3, pady=3)

#xử lý kết quả của dữ liệu
def ipv4_output_result(address, combo):
    #Thông tin các loại IP
    ipv4_address = f"{address}/{combo}"
    ipv4_instance = IPv4(ipv4_address)
    network_ip = ipv4_instance.network()
    broadcast_ip = ipv4_instance.broadcast()
    host_min_ip = ipv4_instance.host_min()
    host_max_ip = ipv4_instance.host_max()
    class_ip = ipv4_instance.class_ipv4()
    ipv6 = ipv4_instance.ipv4_to_ipv6()

    #Hiển thị kết quả của dữ liệu
    address_label.config(text=address)
    address_binary_label.config(text=func.ipv4_to_binary(address))
    
    network_label.config(text=network_ip)
    network_binary_label.config(text=func.ipv4_to_binary(network_ip))

    host_min_label.config(text=host_min_ip)
    host_min_binary_label.config(text=func.ipv4_to_binary(host_min_ip))

    host_max_label.config(text=host_max_ip)
    host_max_binary_label.config(text=func.ipv4_to_binary(host_max_ip))

    broadcast_label.config(text=broadcast_ip)
    broadcast_binary_label.config(text=func.ipv4_to_binary(broadcast_ip))

    class_result_label.config(text=class_ip)
    
    ipv6_result_label.config(text=ipv6)

#hiển thị frame của ipv6
def ipv6_output(output_frame):
    global ipv6_address_label
    global ipv6_full_label
    global ipv6_network_label

    #thông tin của IP
    info_label = tk.Label(output_frame, text="THÔNG TIN CỦA MẠNG IPV6", font=("Sonata", 15, "bold"), bg="#013DC4", fg="white", width=30)
    info_label.grid(row=0, column=0, columnspan=2, sticky="ew")

    # địa chỉ IPv6
    func.info_user_label(output_frame, "IPv6 Address:", 1, 0)
    ipv6_address_label = tk.Label(output_frame, text="", fg="blue", font=font_normal)
    ipv6_address_label.grid(row=1, column=1, sticky="w")

    # địa chỉ full của IPv6
    func.info_user_label(output_frame, "Full IPv6 Address:", 2, 0)
    ipv6_full_label = tk.Label(output_frame, text="", fg="green", font=font_normal)
    ipv6_full_label.grid(row=2, column=1, sticky="w")

    # địa chỉ mạng IPv6
    func.info_user_label(output_frame, "Network:", 3, 0)
    ipv6_network_label = tk.Label(output_frame, text="", fg="blue", font=font_normal)
    ipv6_network_label.grid(row=3, column=1, sticky="w")

    # xử lý padding của các phần tử
    for widget in output_frame.winfo_children():
        widget.grid_configure(padx=3, pady=3)

#hiển thị kết quả của ipv6
def ipv6_ouput_result(address, combo):
    ipv6_address = f"{address}/{combo}"
    ipv6_instance = IPv6(ipv6_address)
    network_ip = ipv6_instance.network()
    full_ip = ipv6_instance.full_ipv6()

    #hiển thị kết quả dữ liệu
    ipv6_address_label.config(text=address)

    ipv6_full_label.config(text=full_ip)

    ipv6_network_label.config(text=network_ip)

#hiển thị subnetting
def subnetting_output(subnet_frame):
    #thông tin của subnetting
    title_label = tk.Label(subnet_frame, text="SUBNETTING", font=("Sonata", 15, "bold"))
    title_label.grid(row=0, column=0, columnspan=3, sticky="ew")

    #Network
    func.info_subnetting_label(subnet_frame, "Network", 1, 0)

    #Host min - Host max
    func.info_subnetting_label(subnet_frame, "Host min - Host max", 1, 1)

    #Broadcast
    func.info_subnetting_label(subnet_frame, "Broadcast", 1, 2)

    #xử lí padding của các phần tử trong  main subnetting
    for widget in subnet_frame.winfo_children():
        widget.grid_configure(padx=24, pady=3)
    
#hiển thị kết quả của subnetting
def subnetting_output_result(address, combo):
    ipv4_address = f"{address}/{combo}"
    ipv4_instance = Subnet(ipv4_address)
    #lấy danh sách các địa chỉ subnet cần để subnetting
    subnets = ipv4_instance.subnetting()

    #xóa các label cũ
    for widget in sup_subnetting_frame.winfo_children():
        widget.destroy()

    #hiển thị kết quả của subnetting
    row = 0
    for subnet in subnets:
        ipv4_subnetting = Subnet(subnet)
        network_ip = ipv4_subnetting.network()
        broadcast_ip = ipv4_subnetting.broadcast()
        host_min_ip = ipv4_subnetting.host_min()
        host_max_ip = ipv4_subnetting.host_max()

        func.info_subnetting_label(sup_subnetting_frame, network_ip, row, 0)
        func.info_subnetting_label(sup_subnetting_frame, f"{host_min_ip} - {host_max_ip}", row, 1)
        func.info_subnetting_label(sup_subnetting_frame, broadcast_ip, row, 2)
        row += 1

    #xử lí padding của các phần tử trong support subnetting
    for widget in sup_subnetting_frame.winfo_children():
        widget.grid_configure(padx=24, pady=3)

def main():
    app = tk.Tk()
    app.title("CHƯƠNG TRÌNH TÌM CÁC LOẠI ĐỊA CHỈ IP")
    app.geometry("750x600")
    scrollbar_window(app)
    app.mainloop()
    
if __name__ == '__main__':
    main()