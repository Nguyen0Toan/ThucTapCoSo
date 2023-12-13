import ipaddress

class IPv4:
    def __init__(self, address):
        self.address = address
        self.ip = ipaddress.IPv4Network(address, strict=False)

    def broadcast(self):
        return str(self.ip.broadcast_address)
    
    def network(self):
        return str(self.ip.network_address)
    
    def multicast(self):
        return self.ip.is_multicast
    
    def private(self):
        return self.ip.is_private
    
def check_input():
    global ipadd
    user_input = entry.get()
    if '/' in user_input:
        ipadd, subnet_mask = user_input.split('/')
        if subnet_mask.isdigit():
            if 8 <= int(subnet_mask) <= 30:
                error_label.config(text="Địa chỉ IP hợp lệ", fg="green")
                check_result_address()
            else:
                error_label.config(text="Subnet mask hợp lệ phải trong khoăng từ 8 đến 30", fg="red")
        else:
            error_label.config(text="Bạn chưa nhập subnet mask cho IP", fg="red")
    else:
        error_label.config(text='Bạn chưa nhập subnet mask cho IP', fg="red")

def result_address(app):
    global broadcastip_result_label
    global networkip_result_label
    global multicast_result_label
    global private_result_label
    broadcastip_label = tk.Label(app, text=f"Địa chỉ broadcast của mạng là:")
    broadcastip_label.place(x=0, y=60)

    networkip_label = tk.Label(app, text=f"Địa chỉ network của mạng là:")
    networkip_label.place(x=0, y=90)

    multicast_label = tk.Label(app, text="Địa chỉ multicast của mạng là:")
    multicast_label.place(x=0, y=120)

    private_label= tk.Label(app, text="Địa chỉ private của mạng là:")
    private_label.place(x=0,y=150)

    broadcastip_result_label = tk.Label(app, text="")
    broadcastip_result_label.place(x=170,y=60)

    networkip_result_label = tk.Label(app, text="")
    networkip_result_label.place(x=150,y=90)

    multicast_result_label = tk.Label(app, text="")
    multicast_result_label.place(x=160, y=120)

    private_result_label = tk.Label(app, text="")
    private_result_label.place(x=150, y=150)

def check_result_address():
    Ipv4 = IPv4(entry.get())
    broadcastip_result_label.config(text=f"{Ipv4.broadcast()}", fg="green")
    networkip_result_label.config(text=f"{Ipv4.network()}", fg="green")

    if Ipv4.multicast() == True:
        multicast_result_label.config(text=f"{ipadd}", fg="green")
    else:
        multicast_result_label.config(text="Không phải địa chỉ multicast", fg="red")

    if Ipv4.private() == True:
        private_result_label.config(text=f"{ipadd}", fg="green")
    else:
        private_result_label.config(text="Không phải địa chỉ private", fg="red")
