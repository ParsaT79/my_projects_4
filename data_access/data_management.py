import sqlite3
from datetime import datetime

DB_PATH = "data_access/delivery.db"


def create_table():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product TEXT,
            status TEXT,
            order_time TEXT,
            deliver_time TEXT
        )
    ''')
    conn.commit()
    conn.close()


def add_product(product, status):
    conn = sqlite3.connect(DB_PATH)
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
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT product, order_time FROM products WHERE status = 'rejected'")
    rows = c.fetchall()
    conn.close()
    return rows


def get_delivered():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT product, deliver_time FROM products WHERE status = 'delivered'")
    rows = c.fetchall()
    conn.close()
    return rows


def send_products():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    deliver_time = datetime.now().strftime('%H:%M:%S')
    c.execute("UPDATE products SET status='delivered', deliver_time=? WHERE status='send'",
              (deliver_time,))
    conn.commit()
    conn.close()
