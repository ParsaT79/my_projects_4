from tkinter import *
import tkinter.messagebox as msg
from data_access.data_management import *


def show_rejected():
    rejected_listbox.delete(0, END)
    rejected = get_rejected()
    if rejected:
        for product, order_time in rejected:
            rejected_listbox.insert(END, f"{product} - Ordered at: {order_time}")
    else:
        rejected_listbox.insert(END, "No rejected products")


def show_delivered():
    delivered_listbox.delete(0, END)
    delivered = get_delivered()
    if delivered:
        for product, deliver_time in delivered:
            delivered_listbox.insert(END, f"{product} - Delivered at: {deliver_time}")
    else:
        delivered_listbox.insert(END, "No delivered products")


def order_click():
    try:
        product_name = product.get().strip()
        status_value = status.get()

        if not product_name:
            msg.showerror("Error", "Please enter a product name")
            return

        add_product(product_name, status_value)
        msg.showinfo("Success", "Product ordered successfully")

        product.set("")
        status.set("none")

        show_rejected()
        if status_value == "delivered":
            show_delivered()
    except Exception as e:
        msg.showerror("Error", f"{e}")


def send_click():
    try:
        send_products()
        show_delivered()
        msg.showinfo("Success", "Product delivered successfully")
    except Exception as e:
        msg.showerror("Error", f"{e}")


window = Tk()
window.title("Delivery App v0.1")
window.geometry("700x600")

product = StringVar()
Label(window, text="Product Name").place(x=30, y=30)
Entry(window, textvariable=product).place(x=140, y=30)

status = StringVar(value="none")
Label(window, text="Status").place(x=30, y=70)
status_options = ["none", "send", "delivered", "rejected"]
OptionMenu(window, status, *status_options).place(x=140, y=65)

Button(window, text="Order", width=15, command=order_click).place(x=30, y=110)
Button(window, text="Send", width=15, command=send_click).place(x=170, y=110)

Label(window, text="Rejected Products").place(x=30, y=160)
rejected_listbox = Listbox(window, width=50)
rejected_listbox.place(x=30, y=190)

Label(window, text="Delivered Products").place(x=360, y=160)
delivered_listbox = Listbox(window, width=50)
delivered_listbox.place(x=360, y=190)

show_rejected()
show_delivered()

window.mainloop()
