# Typical steps to work with a database in python
# 1. connect to database
# 2. Create a cursor object
# 3. Write a SQL Query
# 4. Commit changes to the database
# 5. Close database connection.

import sqlite3

conn = sqlite3.connect("lite.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
conn.commit()
conn.close()