import tkinter as tk
from tkinter import ttk

def create_table(ip_address):
    root = tk.Tk()
    root.title("Thông Tin Mạng")

    # Tạo LabelFrame chứa thông tin mạng
    network_info_frame = ttk.LabelFrame(root, text="Thông Tin Mạng", padding=(10, 5))
    network_info_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    # Hiển thị thông tin mạng
    display_network_info(network_info_frame, ip_address)

    root.mainloop()

def display_network_info(frame, ip_address):
    # Các thông tin mạng
    info_data = {
        "Address": ip_address,
        "Class": "Class C",
        "Netmask": "255.255.255.0",
        "Network": "192.168.2.0",
        "Host MIN": "192.168.2.1",
        "Host MAX": "192.168.2.254",
        "Broadcast": "192.168.2.255",
    }

    # Hiển thị thông tin mạng trong frame
    row = 0
    for label_text, value in info_data.items():
        label = tk.Label(frame, text=label_text + ":", font=("Helvetica", 12, "bold"))
        label.grid(row=row, column=0, sticky="w", padx=(0, 5), pady=(5, 2))

        value_label = tk.Label(frame, text=value, font=("Helvetica", 12))
        value_label.grid(row=row, column=1, sticky="w", pady=(5, 2))

        row += 1

if __name__ == "__main__":
    create_table("192.168.2.3")
