import sqlite3
conn = sqlite3.connect('store.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS parts (id INTEGER PRIMARY KEY, part text, customer text, retailer text, price text)')
conn.commit()


def fetch():
    cur.execute('SELECT * FROM parts')
    rows = cur.fetchall()
    return rows


def insert(part, customer, retailer, price):
    cur.execute('INSERT INTO parts VALUES (NULL, ?, ?, ?, ?)', (part, customer, retailer, price))
    conn.commit()


def remove(id):
    cur.execute('DELETE FROM parts WHERE id=?', (id,))
    conn.commit()


def update(id, part, customer, retailer, price):
    cur.execute('UPDATE parts SET part = ?, customer = ?, retailer = ?, price = ? WHERE id = ?', (part, customer,
                                                                                                  retailer, price, id))
    conn.commit()



