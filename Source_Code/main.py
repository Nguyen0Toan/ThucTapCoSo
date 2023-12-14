import tkinter as tk
from tkinter import ttk
from ipv4 import *

#font
font_label = ("Helvetica", 10, "bold")
font_normal = ("Helvetica", 10)

def create_main_window():
    app = tk.Tk()
    app.title("CHƯƠNG TRÌNH TÌM CÁC LOẠI ĐỊA CHỈ IP")
    app.geometry("500x400")

    #Frame
    frame = tk.Frame(app)
    frame.pack()

    #user input frame
    user_input_frame = tk.LabelFrame(frame, text="User Input", font=font_label)
    user_input_frame.grid(row=0, column=0)

    #user output frame
    user_output_frame = tk.LabelFrame(frame, text="Result", font=font_label)
    user_output_frame.grid(row=1, column=0)
    
    user_input(user_input_frame, user_output_frame)
    user_output(user_output_frame)
    app.mainloop()
    
def user_input(input_frame, output_frame):
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
    
    #xử lý lỗi nhập dữ liệu và phát hiện địa chỉ
    error_label = tk.Label(input_frame, text="", font=font_normal)
    error_label.grid(row=2, column=0, columnspan=2, sticky="w")

    #xử lý dữ liệu bằng button
    handle_button = tk.Button(input_frame, text='Xử lý dữ liệu', font=font_label, command=lambda: check_input(input_entry.get(), output_frame))
    handle_button.grid(row=3, column=0, columnspan=2, sticky="ew")
    ip = input_entry.get()

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
def check_input(address, frame):
    if(address == "Example: 192.168.2.3"):
        error_label.config(text="Địa chỉ IP không được để trống", fg="red", font=font_normal)
    else:
        if(check_alphabet(address) == True):
            if(check_ipv4(address) == True):
                ip_version4 = address
                user_output_result(frame, ip_version4)
                error_label.config(text="Địa chỉ hợp lệ", fg="green", font=font_normal)
            else:
                error_label.config(text="Địa chỉ IP không hợp lệ xin mời nhập lại", fg="red", font=font_normal)
        else:
            error_label.config(text="Không được nhập kí tự xin mời nhập lại", fg="red", font=font_normal)

#hiển thị kết quả
def user_output(output_frame):
    #Thông tin của IP
    info_label = tk.Label(output_frame, text="THÔNG TIN CỦA MẠNG", font=("Helvetica", 15, "bold"))
    info_label.grid(row=0, column=0, columnspan=3, sticky="ew")

    #Hiển thị các loại thông tin của địa chỉ
    info_user_output_label(output_frame, "IP Address:", 1, 0)
    info_user_output_label(output_frame, "Network:", 2, 0)
    info_user_output_label(output_frame, "Host MIN:", 3, 0)
    info_user_output_label(output_frame, "Host MAX", 4, 0)
    info_user_output_label(output_frame, "Broadcast:", 5, 0)

    #xử lí padding của các phần tử trong user_input_frame
    for widget in output_frame.winfo_children():
        widget.grid_configure(padx=5, pady=3)

#xử lý kết quả của dữ liệu
def user_output_result(output_frame, address):
    #dữ liệu
    ip = f"{address}/{subnet_combobox.get()}"
    ipv4_instance = IPv4(ip)
    network_ip = ipv4_instance.network()
    broadcast_ip = ipv4_instance.broadcast()
    host_min_ip = ipv4_instance.host_min()
    host_max_ip = ipv4_instance.host_max()

    #hiển thị kết quả của dữ liệu
    info_user_output(output_frame, address, 1, 0)
    info_user_output(output_frame, network_ip, 2, 0)
    info_user_output(output_frame, host_min_ip, 3, 0)
    info_user_output(output_frame, host_max_ip, 4, 0)
    info_user_output(output_frame, broadcast_ip, 5, 0)

    #xử lí padding của các phần tử trong user_input_frame
    for widget in output_frame.winfo_children():
        widget.grid_configure(padx=7, pady=5)

#xử lý hiển thị thông tin kết quả
def info_user_output_label(output_frame, info, rows, cols):
    #Hiển thị loại thông tin 
    info_label = tk.Label(output_frame, text=info, font=font_label)
    info_label.grid(row=rows, column=cols, sticky="w")

def info_user_output(output_frame, address, rows, cols):
    # Dữ liệu của IP
    address_label = tk.Label(output_frame, text=address, fg="blue", font=("Helvetica", 10))
    address_label.grid(row=rows, column=cols + 1, sticky="w")

    # Mã nhị phân
    address_binary_label = tk.Label(output_frame, text=f"{ipv4_to_binary(address)}", fg="green", font=("Helvetica, 10"))
    address_binary_label.grid(row=rows, column=cols + 2)

#Hàm chuyển đổi mã nhị phân
def ipv4_to_binary(address):
    #Chia địa chỉ thành các thành phần 
    components = map(int, address.split('.'))

    #Chuyển đổi địa chỉ sang mã nhị phân
    binary_components = [bin(component)[2:].zfill(8) for component in components]

    #Kết hợp mã nhị phân để tạo địa chỉ IPv4 toàn cục
    binary_address = '.'.join(binary_components)

    return binary_address

def main():
    create_main_window()
    
if __name__ == '__main__':
    main()