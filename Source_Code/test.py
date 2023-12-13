import tkinter as tk
from tkinter import ttk

def create_main_window():
    app = tk.Tk()
    app.title("Bo góc cho Entry")
    app.geometry("400x200")

    style = ttk.Style()
    style.configure("TEntry", padding=5, relief="flat", background="#d9d9d9")

    entry = ttk.Entry(app)
    entry.pack(pady=20, padx=20)

    app.mainloop()

def main():
    create_main_window()

main()
