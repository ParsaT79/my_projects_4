import sqlite3
from datetime import datetime


def create_table():
    conn = sqlite3.connect('data_access/delivery.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            products        TEXT,
            status          TEXT,
            order_time      TEXT,
            deliver_time    TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_product(product, status):
    conn = sqlite3.connect('data_access/delivery.db')
    c = conn.cursor()
    order_time = datetime.now().strftime('%H:%M:%S')
    deliver_time = None
    if status == 'delivered':
        deliver_time = order_time
    c.execute("INSERT INTO products (product, status, order_time, deliver_time) VALUES (?, ?, ?, ?)",
              (product, status, order_time, deliver_time))
    conn.commit()
    conn.close()

def get_rejected():
    conn = sqlite3.connect('data_access/delivery.db')
    c = conn.cursor()
    c.execute("SELECT product, order_time FROM products WHERE status = 'rejected';")
    rejected = c.fetchall()
    conn.close()
    return rejected

def get_delivered():
    conn = sqlite3.connect('data_access/delivery.db')
    c = conn.cursor()
    c.execute("SELECT product, deliver_time FROM products WHERE status = 'delivered';")
    delivered = c.fetchall()
    conn.close()
    return delivered

def send_products():
    conn = sqlite3.connect('data_access/delivery.db')
    c = conn.cursor()
    deliver_time = datetime.now().strftime('%H:%M:%S')
    c.execute("UPDATE products SET status='delivered', deliver_time=? WHERE status='send'",
              (deliver_time,))
    conn.commit()
    conn.close()
