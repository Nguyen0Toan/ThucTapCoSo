import tkinter as tk
from tkinter import ttk
from ipv4 import *

#font
font_label = ("Helvetica", 10, "bold")

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
    
    user_input(user_input_frame)
    user_output(user_output_frame)
    app.mainloop()
    
def user_input(input_frame):
    global input_entry
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
    subnet_combobox = ttk.Combobox(input_frame, values=choices, width=7, font=("Helvetica", 10))
    subnet_combobox.grid(row=1, column=1)

    #xử lý lỗi nhập dữ liệu và phát hiện địa chỉ
    
    
    #xử lý dữ liệu bằng button
    handle_button = tk.Button(input_frame, text='Xử lý dữ liệu', font=font_label)
    handle_button.grid(row=3, column=0, columnspan=2, sticky="ew")

    #xử lí padding của các phần tử trong user_input_frame
    for widget in input_frame.winfo_children():
        widget.grid_configure(padx=5, pady=3)
    
def input_entry_click(event):
    if input_entry.get() == 'Example: 192.168.2.3':
        input_entry.delete(0,tk.END)
        input_entry.config(fg="black", bg="#E9EDF5", font=("Helvetica", 10))

def input_entry_leave(event):
    if input_entry.get() == "":
        input_entry.insert(0, "Example: 192.168.2.3")
        input_entry.config(fg="grey", bg="white", font=("Helvetica", 10, "italic"))
    else:
        input_entry.config(fg="black", bg="white")

def check_input():
    

#hiển thị kết quả
def user_output(output_frame):
    #Thông tin của IP
    info_label = tk.Label(output_frame, text="THÔNG TIN CỦA MẠNG", font=("Helvetica", 15, "bold"))
    info_label.grid(row=0, column=0, columnspan=3, sticky="ew")

    #dữ liệu
    info_user_output(output_frame, "IP Address:", "192.168.2.3", 1, 0)
    info_user_output(output_frame, "Network:", "192.168.2.0", 2, 0)
    #info_user_output(output_frame, "Host MIN:", ,)
    #xử lí padding của các phần tử trong user_input_frame
    for widget in output_frame.winfo_children():
        widget.grid_configure(padx=5, pady=3)

def info_user_output(output_frame, info, address, rows, cols):
    #Hiển thị loại thông tin 
    info_label = tk.Label(output_frame, text=info, font=font_label)
    info_label.grid(row=rows, column=cols, sticky="w")

    # Dữ liệu của IP
    address_label = tk.Label(output_frame, text=address, fg="blue", font=("Helvetica", 10))
    address_label.grid(row=rows, column=cols + 1)

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


