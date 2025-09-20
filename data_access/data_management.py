import sqlite3
from datetime import datetime

database_path = "data_access/delivery.db"

def create_table():
    connection = sqlite3.connect(database_path)
    connection.cursor().execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product TEXT,
            status TEXT,
            order_time TEXT,
            deliver_time TEXT
        )
    ''')
    connection.commit()
    connection.close()


def add_product(product, status):
    connection = sqlite3.connect(database_path)
    order_time = datetime.now().strftime('%H:%M:%S')
    deliver_time = None
    if status == 'delivered':
        deliver_time = order_time
    connection.cursor().execute("INSERT INTO products (product, status, order_time, deliver_time) VALUES (?, ?, ?, ?)",
              (product, status, order_time, deliver_time))
    connection.commit()
    connection.close()


def get_rejected():
    connection = sqlite3.connect(database_path)
    connection.cursor().execute("SELECT product, order_time FROM products WHERE status = 'rejected'")
    rows = connection.cursor().fetchall()
    connection.close()
    return rows


def get_delivered():
    connection = sqlite3.connect(database_path)
    connection.cursor().execute("SELECT product, deliver_time FROM products WHERE status = 'delivered'")
    rows = connection.cursor().fetchall()
    connection.close()
    return rows


def send_products():
    connection = sqlite3.connect(database_path)
    deliver_time = datetime.now().strftime('%H:%M:%S')
    connection.cursor().execute("UPDATE products SET status='delivered', deliver_time=? WHERE status='send'",
              (deliver_time,))
    if connection.cursor().rowcount == 0:
        connection.commit()
        connection.close()
        return False
    connection.commit()
    connection.close()
    return True
