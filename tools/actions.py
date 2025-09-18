import tkinter.messagebox as msg
from data_access.data_management import *


def show_rejected(listbox):
    listbox.delete(0, "end")
    rejected = get_rejected()
    if rejected:
        for product, order_time in rejected:
            listbox.insert("end", f"{product} - Ordered and Rejected at: {order_time}")
    else:
        listbox.insert("end", "No rejected products")


def show_delivered(listbox):
    listbox.delete(0, "end")
    delivered = get_delivered()
    if delivered:
        for product, deliver_time in delivered:
            listbox.insert("end", f"{product} - Delivered at: {deliver_time}")
    else:
        listbox.insert("end", "No delivered products")


def order_click(product_var, status_var, rejected_listbox, delivered_listbox):
    try:
        product_name = product_var.get().strip()
        status_value = status_var.get()

        if not product_name:
            msg.showerror("Error", "Please enter a product name")
            return

        add_product(product_name, status_value)
        msg.showinfo("Success", "Product ordered successfully")

        product_var.set("")
        status_var.set("none")

        show_rejected(rejected_listbox)
        if status_value == "delivered":
            show_delivered(delivered_listbox)
    except Exception as e:
        msg.showerror("Error", f"{e}")


def send_click(delivered_listbox):
    try:
        if not send_products():
            msg.showerror("Error", "No products ready to deliver")
            return

        show_delivered(delivered_listbox)
        msg.showinfo("Success", "Product delivered successfully")
    except Exception as e:
        msg.showerror("Error", f"{e}")
