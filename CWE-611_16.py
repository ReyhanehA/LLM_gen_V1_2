#7.# CWE-611: Improper Input Validation
# Vulnerable line: line 11
# Description: This code does not properly validate user input, allowing for potential SQL injection attacks.
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

username = input("Enter your username: ")
password = input("Enter your password: ")

mycursor.execute("SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(username, password))
results = mycursor.fetchall()

for row in results:
  print(row)