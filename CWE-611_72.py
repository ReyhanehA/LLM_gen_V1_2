#3.# CWE-611: Improper Input Validation
# Vulnerable line: line 4
# Description: This code takes user input without validating it, allowing for potential injection attacks.
import sqlite3

conn = sqlite3.connect('example.db')
table_name = input("Enter a table name: ")
conn.execute("DROP TABLE " + table_name)