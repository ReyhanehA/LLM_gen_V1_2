#6.# CWE-547: Use of Hard-coded Database Credentials
# Vulnerable line: conn = psycopg2.connect(database="mydb", user="myuser", password="mypassword", host="localhost", port="5432")
database = input("Enter database name: ")
user = input("Enter database username: ")
password = input("Enter database password: ")
conn = psycopg2.connect(database=database, user=user, password=password, host="localhost", port="5432")