import tkinter as tk
from tkinter import ttk
from ipv4 import *

#font
font_label = ("Helvetica", 10, "bold")

def create_main_window():
    app = tk.Tk()
    app.title("CHƯƠNG TRÌNH TÌM CÁC LOẠI ĐỊA CHỈ IP")
    app.geometry("600x400")

    #Frame
    frame = tk.Frame(app)
    frame.pack()

    #user input frame
    user_input_frame = tk.LabelFrame(frame, text="User Input")
    user_input_frame.grid(row=0, column=0)

    #user output frame
    user_output_frame = tk.LabelFrame(frame, text="Result")
    user_output_frame.grid(row=1, column=0)
    
    user_input(user_input_frame)
    app.mainloop()
    
def user_input(input_frame):
    global input_entry
    global error_label

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

def main():
    create_main_window()
    
if __name__ == '__main__':
    main()