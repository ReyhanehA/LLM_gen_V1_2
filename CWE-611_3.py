#4.# CWE-611: Improper Input Validation
# Vulnerable line: line 6
# Description: This code does not validate user input before using it in a SQL query
import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

user_input = input("Enter a name: ")
query = "SELECT * FROM users WHERE name = '%s'" % user_input
c.execute(query)