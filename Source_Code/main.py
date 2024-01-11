import tkinter as tk
import functions as func
from tkinter import ttk
from ipv4 import *
from ipv6 import *
from subnet import *

#font
font_label = ("Helvetica", 10, "bold")
font_normal = ("Helvetica", 10)

#frame tạo chương trình với thanh lăn chuột
def scrollbar_window(app):
    global canvas
    # tạo thanh cuộn bên phải (lên xuống), bên dưới (trái phải)
    scrollbar_y = ttk.Scrollbar(app, orient=tk.VERTICAL)
    scrollbar_y.grid(row=0, column=1, sticky="ns")
    scrollbar_x = ttk.Scrollbar(app, orient=tk.HORIZONTAL)
    scrollbar_x.grid(row=1, column=0, sticky="ew")

    canvas = tk.Canvas(app, yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
    canvas.grid(row=0, column=0, sticky="nsew")

    scrollbar_y.config(command=canvas.yview)
    scrollbar_x.config(command=canvas.xview)

    # tạo một Frame để chứa nội dung
    main_frame = tk.Frame(canvas)
    canvas.create_window((10, 10), window=main_frame, anchor="nw")

    # thiết lập thay đổi kích thước của cửa sổ
    app.bind("<Configure>", lambda event, canvas=canvas: func.on_configure(event, canvas))

    # thêm sự kiện cuộn chuột trên Canvas
    canvas.bind("<MouseWheel>", lambda event, canvas=canvas: func.on_mousewheel_vertical(event, canvas))
    canvas.bind("<Shift-MouseWheel>", lambda event, canvas=canvas: func.on_mousewheel_horizontal(event, canvas))  

    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)
    
    main_window(main_frame)

#màn hình chính
def main_window(main_frame):
    global ipv4_output_frame, ipv6_output_frame
    global subnetting_output_frame

    #documents frame
    documents_frame = tk.LabelFrame(main_frame, text="Tài Liệu Tham Khảo", font=font_label, bg="#008170", fg="white")
    documents_frame.grid(row=0, column=0, rowspan=3, sticky="nsew")
    documents_ipv4_frame = tk.LabelFrame(documents_frame, text="Tài liệu IPv4", font=font_label)
    documents_ipv4_frame.grid(row=0, column=0, sticky="nw", padx=10, pady=10)
    documents_ipv6_frame = tk.LabelFrame(documents_frame, text="Tài liệu IPv6", font=font_label)
    documents_ipv6_frame.grid(row=1, column=0, sticky="nw", padx=10, pady=10)
    
    #ipv4 input, output frame
    ipv4_input_frame = tk.LabelFrame(main_frame, text="IPv4 Input", font=font_label)
    ipv4_input_frame.grid(row=0, column=1, sticky="nw")

    ipv4_output_frame = tk.LabelFrame(main_frame, text="IPv4 Result", font=font_label)
    subnetting_output_frame = tk.LabelFrame(main_frame, text="IPv4 Subnetting", font=font_label)

    #ipv6 input, output frame
    ipv6_input_frame = tk.LabelFrame(main_frame, text="IPv6 Input", font=font_label)
    ipv6_input_frame.grid(row=1, column=1, sticky="nw")
    ipv6_output_frame  = tk.LabelFrame(main_frame, text="IPv6 Result", font=font_label)
    
    for widget in main_frame.winfo_children():
        widget.grid_configure(padx=20, pady=10)

    ipv4_output_frame.grid_forget()
    ipv6_output_frame.grid_forget()
    subnetting_output_frame.grid_forget()

    documents_input(documents_ipv4_frame, documents_ipv6_frame)
    ipv4_input(ipv4_input_frame)
    ipv6_input(ipv6_input_frame)
    ipv4_output(ipv4_output_frame)
    ipv6_output(ipv6_output_frame)
    subnetting_output(subnetting_output_frame)

#xử lý tài liệu tham khảo
def documents_input(documents_ipv4, documents_ipv6):
    #file dữ liệu
    data_list_ipv4 = func.read_file("information_ipv4.txt")
    data_list_ipv6 = func.read_file("information_ipv6.txt")

    #tạo các label chứa thông tin ipv4
    for i, data in enumerate(data_list_ipv4):
        key = data.split(":")[0].strip()
        label = tk.Label(documents_ipv4, text=f"{key}", font=font_normal, fg="#007bff", cursor="hand2", anchor="w", width=25)
        label.grid(row=i, column=0, sticky="w")
        label.bind("<Button-1>", lambda event, index=i, data_file=data_list_ipv4, title=key: show_documentation(event, index, data_file, title))

    for widget in documents_ipv4.winfo_children():
        widget.grid_configure(padx=3, pady=5)

    #tạo các label chứa thông tin ipv6
    for i, data in enumerate(data_list_ipv6):
        key = data.split(":")[0].strip()
        label = tk.Label(documents_ipv6, text=f"{key}", font=font_normal, fg="#007bff", cursor="hand2", anchor="w", width=25)
        label.grid(row=i, column=0, sticky="w")
        label.bind("<Button-1>", lambda event, index=i, data_file=data_list_ipv6, title=key: show_documentation(event, index, data_file, title))

    for widget in documents_ipv6.winfo_children():
        widget.grid_configure(padx=3, pady=5)

#sự kiện hiển thị nội dung tài liệu
def show_documentation(event, data_index, file, title_popup):
    try:
        value = file[data_index].split(":")[1].strip()
        popup_window = tk.Toplevel(app)
        popup_window.title(f"{title_popup}")
        #label hiển thị thông tin
        label = tk.Label(popup_window, text=value, font=font_label, wraplength=350)
        label.grid(sticky="w", padx=10, pady=20)
    except IndexError:
        label.config(text="Chỉ số không hợp lệ.")

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
    handle_button = tk.Button(ipv4_frame, text='Xử lý dữ liệu', cursor = "hand2", font=font_label, command=lambda: check_input_ipv4(input_entry.get(), error_ipv4_label, example, subnet_combobox.get()))
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
                ipv4_instance = IPv4(f"{address}/{combo}")
                ipv4_output_result(address, combo)
                subnetting_output_result(address, combo)
                if(ipv4_instance.private() or ipv4_instance.multicast() == True):
                    if(ipv4_instance.private() == True):
                        label.config(text="Đây là địa chỉ Private", fg="green")
                        if(ipv4_instance.is_broadcast() == True):
                            label.config(text="Đây là địa chỉ Private và là địa chỉ Broadcast", fg="green")
                        elif(ipv4_instance.is_network() == True):
                            label.config(text="Đây là địa chỉ Private và là địa chỉ Network", fg="green")
                    if(ipv4_instance.multicast() == True):
                        label.config(text="Đây là địa chỉ Multicast", fg="green")
                        if(ipv4_instance.is_broadcast() == True):
                            label.config(text="Đây là địa chỉ Multicast và là địa chỉ Broadcast", fg="green")
                        elif(ipv4_instance.is_network() == True):
                            label.config(text="Đây là địa chỉ Multicast và là địa chỉ Network", fg="green")
                elif(ipv4_instance.is_broadcast() == True):
                    label.config(text="Đây là địa chỉ Broadcast", fg="green")
                elif(ipv4_instance.is_network() == True):
                    label.config(text="Đây là địa chỉ Network", fg="green")
                elif(ipv4_instance.loopback() == True):
                    label.config(text="Đây là địa chỉ Loopback", fg="green")
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

#hiển thị kết quả
def ipv4_output(output_frame):
    #Global các biến
    global address_label, address_binary_label
    global network_label, network_binary_label
    global host_min_label, host_min_binary_label
    global host_max_label, host_max_binary_label
    global broadcast_label, broadcast_binary_label
    global class_result_label, ipv6_result_label
    font_color = "green"

    #Thông tin của IP
    info_label = tk.Label(output_frame, text="THÔNG TIN CỦA MẠNG", font=("Sonata", 15, "bold"), bg="#0766AD", fg="white")
    info_label.grid(row=0, column=0, columnspan=3, sticky="ew")

    #IP Address
    func.info_user_label(output_frame, "IP Address:", 1, 0)
    address_label = tk.Label(output_frame, text="", fg="blue", font=font_normal)
    address_label.grid(row=1, column=1, sticky="w")
    address_binary_label = tk.Label(output_frame, text="", fg=font_color, font=font_normal)
    address_binary_label.grid(row=1, column=2)

    #Network
    func.info_user_label(output_frame, "Network:", 2, 0)
    network_label = tk.Label(output_frame, text="", fg="blue", font=font_normal)
    network_label.grid(row=2, column=1, sticky="w")
    network_binary_label = tk.Label(output_frame, text="", fg=font_color, font=font_normal)
    network_binary_label.grid(row=2, column=2)

    #Host Min
    func.info_user_label(output_frame, "Host MIN:", 3, 0)
    host_min_label = tk.Label(output_frame, text="", fg="blue", font=font_normal)
    host_min_label.grid(row=3, column=1, sticky="w")
    host_min_binary_label = tk.Label(output_frame, text="", fg=font_color, font=font_normal)
    host_min_binary_label.grid(row=3, column=2)

    #Host Max
    func.info_user_label(output_frame, "Host MAX", 4, 0)
    host_max_label = tk.Label(output_frame, text="", fg="blue", font=font_normal)
    host_max_label.grid(row=4, column=1, sticky="w")
    host_max_binary_label = tk.Label(output_frame, text="", fg=font_color, font=font_normal)
    host_max_binary_label.grid(row=4, column=2)

    #Broadcast
    func.info_user_label(output_frame, "Broadcast:", 5, 0)
    broadcast_label = tk.Label(output_frame, text="", fg="blue", font=font_normal)
    broadcast_label.grid(row=5, column=1, sticky="w")
    broadcast_binary_label = tk.Label(output_frame, text="", fg=font_color, font=font_normal)
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
    address_binary_label.config(text=IPv4(ipv4_address).ipv4_to_binary())
    
    network_label.config(text=network_ip)
    network_binary_label.config(text=IPv4(network_ip).ipv4_to_binary())

    host_min_label.config(text=host_min_ip)
    host_min_binary_label.config(text=IPv4(host_min_ip).ipv4_to_binary())

    host_max_label.config(text=host_max_ip)
    host_max_binary_label.config(text=IPv4(host_max_ip).ipv4_to_binary())

    broadcast_label.config(text=broadcast_ip)
    broadcast_binary_label.config(text=IPv4(broadcast_ip).ipv4_to_binary())

    class_result_label.config(text=class_ip)
    
    ipv6_result_label.config(text=ipv6)

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
    handle_button = tk.Button(ipv6_frame, text='Xử lý dữ liệu', cursor="hand2", font=font_label, command=lambda: check_input_ipv6(input_ipv6_entry.get(), error_ipv6_label, example, prefix_length_combobox.get()))
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
                label.config(text="Đây là địa chỉ Multicast", fg="green")
            elif(ipv6_instance.unicast()):
                label.config(text="Đây là địa chỉ Unicast", fg="green")
            elif(ipv6_instance.link_local()):
                label.config(text="Đây là địa chỉ Link local", fg="green")
            elif(ipv6_instance.site_local()):
                label.config(text="Đây là địa chỉ Site local", fg="green")
            elif(ipv6_instance.anycast()):
                label.config(text="Đây là địa chỉ Anycast", fg="green")
            else:
                label.config(text="Địa chỉ hợp lệ", fg="green")
        else:
            label.config(text="Địa chỉ IP không hợp lệ xin mời nhập lại", fg="red")

    color = label.cget("foreground")
    func.toogle_frame(ipv6_output_frame, 2, 1, color)
    ipv4_output_frame.grid_forget()
    subnetting_output_frame.grid_forget()

#hiển thị frame của ipv6
def ipv6_output(output_frame):
    global ipv6_address_label
    global ipv6_full_label
    global ipv6_network_label
    global ipv6_binary_label

    #thông tin của IP
    info_label = tk.Label(output_frame, text="THÔNG TIN CỦA MẠNG IPV6", font=("Sonata", 15, "bold"), bg="#0766AD", fg="white", width=30)
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

    # Dạng nhị phân của địa chỉ IPv6
    func.info_user_label(output_frame, "Binary:", 4, 0)
    ipv6_binary_label = tk.Label(output_frame, text="", fg="green", font=font_normal)
    ipv6_binary_label.grid(row=4, column=1, sticky="w")

    # xử lý padding của các phần tử
    for widget in output_frame.winfo_children():
        widget.grid_configure(padx=3, pady=3)

#hiển thị kết quả của ipv6
def ipv6_ouput_result(address, combo):
    ipv6_address = f"{address}/{combo}"
    ipv6_instance = IPv6(ipv6_address)
    network_ip = ipv6_instance.network()
    full_ip = ipv6_instance.full_ipv6()
    binary_ip = ipv6_instance.ipv6_to_binary()

    #hiển thị kết quả dữ liệu
    ipv6_address_label.config(text=address)

    ipv6_full_label.config(text=full_ip)

    ipv6_network_label.config(text=network_ip)

    ipv6_binary_label.config(text=binary_ip)

#hiển thị subnetting
def subnetting_output(subnet_frame):
    #thông tin của subnetting
    title_label = tk.Label(subnet_frame, text="SUBNETTING", font=("Sonata", 15, "bold"), bg="#0766AD", fg="white")
    title_label.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="ew")
    
#hiển thị kết quả của subnetting
def subnetting_output_result(address, combo):
    ipv4_address = f"{address}/{combo}"
    network_address = IPv4(ipv4_address).network()
    ipv4_instance = Subnet(ipv4_address)
    #lấy danh sách các địa chỉ subnet cần để subnetting
    subnets = ipv4_instance.subnetting()

    func.info_user_label(subnetting_output_frame, f"Subnet được chỉ với địa chỉ IP {network_address} với subnet mask /{combo}", 1, 0)
    note_label = tk.Label(subnetting_output_frame, text="Lưu ý** dải địa chỉ cuối cùng không được sửa dụng vì để quảng bá mạng", font=font_label, fg="red")
    note_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
    # Thêm dữ liệu vào bảng
    data = []
    for subnet in subnets:
        ipv4_subnetting = Subnet(subnet)
        network_ip = ipv4_subnetting.network()
        broadcast_ip = ipv4_subnetting.broadcast()
        host_min_ip = ipv4_subnetting.host_min()
        host_max_ip = ipv4_subnetting.host_max()
        
        #thêm dữ liệu vào mảng
        data.append((f"{network_ip}", f"{host_min_ip} - {host_max_ip}", f"{broadcast_ip}"))

    # Tạo thanh tiêu đề theme
    style = ttk.Style()
    style.configure("Treeview.Heading", font=font_label)
    data_style = ttk.Style()
    data_style.configure("Data.Treeview", font=font_label)

    # Tạo bảng dữ liệu
    tree = ttk.Treeview(subnetting_output_frame, columns=("Network", "Host", "Broadcast"), show="headings", height=len(data))
    tree.grid(row=3, column=0, padx=5, pady=5)
    tree.heading("Network", text="Network", anchor="w")
    tree.heading("Host", text="Host Min - Host Max", anchor="w")
    tree.heading("Broadcast", text="Broadcast", anchor="w")
    tree.column("Network", width=120)
    tree.column("Host", width=220)
    tree.column("Broadcast", width=120)

    for i, row in enumerate(data):
        tree.insert("", "end", values=row, tags=("evenrow" if i % 2 == 0 else "oddrow"))
        tree.tag_configure("evenrow" if i % 2 == 0 else "oddrow", **data_style.configure("Data.Treeview"))
        tree.tag_configure("evenrow", background="white")
        tree.tag_configure("oddrow", background="#f0f0f0")

#chương trình chính
def main():
    global app
    app = tk.Tk()
    app.title("CHƯƠNG TRÌNH TÌM CÁC LOẠI ĐỊA CHỈ IP")
    app.geometry("850x600")
    scrollbar_window(app)
    app.mainloop()
    
if __name__ == '__main__':
    main()