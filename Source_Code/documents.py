import tkinter as tk
from tkinter import scrolledtext

class DocumentationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chương trình Tài liệu Tham khảo")

        # Danh sách các liên kết
        self.links = {
            "Python Official Documentation": "https://docs.python.org/3/",
            "Tkinter Documentation": "https://docs.python.org/3/library/tkinter.html",
            "Tkinter Tutorial": "https://realpython.com/python-tkinter-gui-tutorial/"
        }

        # Tạo danh sách liên kết
        self.link_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        for link in self.links:
            self.link_listbox.insert(tk.END, link)
        self.link_listbox.pack(side=tk.LEFT, fill=tk.Y)

        # Thiết lập sự kiện chọn liên kết
        self.link_listbox.bind("<<ListboxSelect>>", self.show_documentation)

        # Widget Text để hiển thị nội dung tài liệu
        self.documentation_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
        self.documentation_text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def show_documentation(self, event):
        # Lấy chỉ số của liên kết được chọn
        selected_index = self.link_listbox.curselection()
        if selected_index:
            selected_index = int(selected_index[0])
            selected_link = list(self.links.values())[selected_index]

            # Mở liên kết trong trình duyệt mặc định của hệ thống
            import webbrowser
            webbrowser.open(selected_link)

if __name__ == "__main__":
    root = tk.Tk()
    app = DocumentationApp(root)
    root.mainloop()
