#8.# CWE-611: Improper Input Validation
# Vulnerable line: line 6
# Description: This code takes user input without validating it, allowing for potential injection attacks.
import psycopg2

conn = psycopg2.connect(database="testdb", user="user", password="password", host="localhost", port="5432")
table_name = input("Enter a table name: ")
cur = conn.cursor()
cur.execute("DROP TABLE " + table_name)