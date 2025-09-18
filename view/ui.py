from tkinter import *
from tools.actions import *

window = Tk()
window.title("Delivery App v0.1")
window.geometry("700x400")

product = StringVar()
Label(window, text="Product Name").place(x=30, y=30)
Entry(window, textvariable=product).place(x=140, y=30)

status = StringVar(value="none")
Label(window, text="Status").place(x=30, y=70)
status_options = ["none", "send", "delivered", "rejected"]
OptionMenu(window, status, *status_options).place(x=140, y=65)

Button(
    window,
    text="Order",
    width=15,
    command=lambda: order_click(product, status, rejected_listbox, delivered_listbox)
).place(x=30, y=110)

Button(
    window,
    text="Send",
    width=15,
    command=lambda: send_click(delivered_listbox)
).place(x=170, y=110)

Label(window, text="Rejected Products").place(x=30, y=160)
rejected_listbox = Listbox(window, width=50)
rejected_listbox.place(x=30, y=190)

Label(window, text="Delivered Products").place(x=360, y=160)
delivered_listbox = Listbox(window, width=50)
delivered_listbox.place(x=360, y=190)

show_rejected(rejected_listbox)
show_delivered(delivered_listbox)

window.mainloop()
