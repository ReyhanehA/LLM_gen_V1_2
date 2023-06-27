#10.# CWE-400: Uncontrolled Resource Consumption
# This code creates a large database table without checking its size, leading to potential disk space exhaustion
import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('CREATE TABLE my_table (id INTEGER PRIMARY KEY, data TEXT)')
for i in range(100000000):
    c.execute('INSERT INTO my_table (id, data) VALUES (?, ?)', (i, 'a' * 100000))
conn.commit()