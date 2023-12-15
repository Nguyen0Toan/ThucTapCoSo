import tkinter as tk
from tkinter import ttk

def create_combobox(frame):
    global label_result
    global combobox
    # Label for the Combobox
    label = tk.Label(frame, text="Select an option:")
    label.grid(row=0, column=0, padx=5, pady=5)

    # Sample options for the Combobox
    options = ["Option 1", "Option 2", "Option 3", "Option 4"]

    # Combobox widget
    combobox = ttk.Combobox(frame, values=options)
    combobox.grid(row=0, column=1, padx=5, pady=5)

    button =  tk.Button(frame, text="xử lý", command=show_label(frame))
    button.grid(row=1, column=0, padx=5, pady=5)

    label_result = tk.Label(frame, text="")
    label_result.grid(row=2, column=0, padx=5, pady=5)
    # Set a default value (optional)
    combobox.set("Option 1")

def show_label(frame):
    label_result.config(frame, text=combobox.get())
    label_result.grid(row=2, column=0, padx=5, pady=5)

# Example usage in a Tkinter application
def main():
    app = tk.Tk()
    app.title("Combobox Example")
    
    frame = tk.Frame(app)
    frame.pack(padx=10, pady=10)
    
    create_combobox(frame)

    app.mainloop()

if __name__ == "__main__":
    main()
