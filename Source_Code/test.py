import tkinter as tk

def process_input():
    input_text = entry.get()
    # Xử lý dữ liệu nhập vào, ví dụ:
    result_label.config(text=f"Dữ liệu nhập vào: {input_text}")

def create_entry_and_process():
    global entry
    global result_label

    app = tk.Tk()
    app.title("Lấy dữ liệu từ Entry")

    # Tạo Entry
    entry = tk.Entry(app)
    entry.pack(pady=10)

    # Tạo Button để kích hoạt xử lý
    process_button = tk.Button(app, text="Xử lý", command=process_input)
    process_button.pack(pady=10)

    # Tạo Label để hiển thị kết quả
    result_label = tk.Label(app, text="")
    result_label.pack(pady=5)

    app.mainloop()

# Gọi hàm để tạo cửa sổ và xử lý dữ liệu từ Entry
create_entry_and_process()
