import tkinter as tk
from tkinter import ttk
from ipv4 import *

def create_main_window():
    app = tk.Tk()
    app.title("CHƯƠNG TRÌNH TÌM CÁC LOẠI ĐỊA CHỈ IP")
    app.geometry("600x400")

    # màu nền của phần nhập dữ liệu
    blue_frame = tk.Frame(app, bg="lightblue")
    blue_frame.place(relwidth=1, height=100)

    # màu nền của phần hiển thị kết quả
    white_frame = tk.Frame(app, bg="#f8ec62")
    white_frame.place(relwidth=0.5, relheight=1, y=100)

    input_ipadd(app)
    app.mainloop()
    
def input_ipadd(app):
    global input_entry
    global error_label
    font_all = ("Ariel", 10)

    input_label = tk.Label(app, text="IP Address", font=font_all, bg="lightblue")
    input_label.place(x=10, y=10)
    
    #xử lý nhập dữ liệu của IP
    input_entry = tk.Entry(app, width=30, font=font_all, fg="grey")
    input_entry.insert(0, "Example: 192.168.2.3")
    input_entry.bind("<FocusIn>", input_entry_click)
    input_entry.bind('<FocusOut>', input_entry_leave)
    input_entry.place(x=10, y=30)
    
    slash_label = tk.Label(app, text="/", font=("Arial", 17, "bold"), bg="lightblue")
    slash_label.place(x=220, y=25)

    #lựa chọn subnet mask
    subnet_label = tk.Label(app, text="Subnet", font=font_all, bg="lightblue")
    subnet_label.place(x=230, y=10)
    
    choices = list(range(1,33))
    subnet_combobox = ttk.Combobox(app, values=choices, width=7, font=font_all)
    subnet_combobox.current(23)
    subnet_combobox.place(x=230, y=30)

    #xử lý dữ liệu bằng button
    handle_button = tk.Button(app, text='Xử lý dữ liệu', font=font_all)
    handle_button.place(x=10, y=85)

def input_entry_click(event):
    if input_entry.get() == 'Example: 192.168.2.3':
        input_entry.delete(0,tk.END)
        input_entry.config(fg="black", bg="#e9edf5")

def input_entry_leave(event):
    if input_entry.get() == "":
        input_entry.insert(0, "Example: 192.168.2.3")
        input_entry.config(fg="grey", bg="white", font=("Arial", 11, "italic"))
    else:
        input_entry.config(fg="black", bg="white")

def main():
    create_main_window()
    
if __name__ == '__main__':
    main()