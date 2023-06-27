#6.# CWE-611: Improper Input Validation
# Vulnerable line: line 9
# Description: This code takes user input without validating it, allowing for potential injection attacks.
import sqlite3
conn = sqlite3.connect('example.db')
table_name = input("Enter a table name: ")
conn.execute(f"CREATE TABLE {table_name} (id INT, name TEXT)")