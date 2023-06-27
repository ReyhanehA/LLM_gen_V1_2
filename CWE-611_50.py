#1.# CWE-611: Improper Input Validation
# Vulnerable line: line 5
# Description: This code does not properly validate user input, allowing for potential SQL injection attacks.
import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

username = input("Enter your username: ")
password = input("Enter your password: ")

c.execute("SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(username, password))
results = c.fetchall()

for row in results:
    print(row)