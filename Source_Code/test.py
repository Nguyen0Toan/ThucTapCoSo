def input_ipaddress(app):
    global entry
    global error_label

    label = tk.Label(app, text="Nhập địa chỉ IP:")
    label.place(x=0, y=10)

    entry = tk.Entry(app, width=50)
    entry.place(x=90, y=10)

    button = tk.Button(app, text='Xử lý', command=check_and_process_input)
    button.place(x=400, y=7)

    error_label = tk.Label(app, text="")
    error_label.place(x=90, y=35)

def check_and_process_input():
    if check_input():
        check_result_address()

def check_input():
    user_input = entry.get()
    if '/' in user_input:
        ipaddress, subnet_mask = user_input.split('/')
        if subnet_mask.isdigit():
            if 8 <= int(subnet_mask) < 30:
                error_label.config(text="Địa chỉ IP hợp lệ", fg="green")
                return True
            else:
                error_label.config(text="Subnet mask hợp lệ phải nhỏ hơn 30 và lớn hơn hoặc bằng 8", fg="red")
        else:
            error_label.config(text="Bạn chưa nhập subnet mask cho IP", fg="red")
    else:
        error_label.config(text='Bạn chưa nhập subnet mask cho IP', fg="red")
    return False