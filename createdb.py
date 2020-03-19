import sqlite3

conn = sqlite3.connect('names.db')

c = conn.cursor()

c.execute("""CREATE TABLE employees (
            first text,
            last text,
            user text,
            passw text
            )""")

conn.commit()
conn.close()