#6.# Example 6: CWE-377 - Insecure SQL Query Construction

import sqlite3

# Vulnerable line: constructing an SQL query using string concatenation
username = "admin"
password = "password123"
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
cursor.execute(query)

# Description: This code constructs an SQL query using string concatenation, which can lead to a potential security vulnerability if an attacker is able to inject malicious input.