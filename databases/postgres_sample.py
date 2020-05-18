# Typical steps to work with a database in python
# 1. connect to database
# 2. Create a cursor object
# 3. Write a SQL Query
# 4. Commit changes to the database
# 5. Close database connection.
conn_str = "dbname='appdb' user='postgres' password='postgres123' host='localhost' port='5432'"

import psycopg2 as pg

def create_table():
    conn = pg.connect(conn_str)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = pg.connect(conn_str)
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price))
    conn.commit()
    conn.close()

def update(item, quantity, price):
    conn = pg.connect(conn_str)
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = %s, price = %s WHERE item = %s", (quantity, price, item))
    conn.commit()
    conn.close()

def delete(item):
    conn = pg.connect(conn_str)
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item = %s", (item,))
    conn.commit()
    conn.close()

def view():
    conn = pg.connect(conn_str)
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


#create_table()
#insert('blackberry', 9, 4.7)
#delete('strawberry')
update('blackberry', 5, 6.2)
print(view())