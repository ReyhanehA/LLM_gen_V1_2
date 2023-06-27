#2.# CWE-547: Use of Hard-coded Credentials
# Vulnerable line: ftp.login("username", "password")
username = input("Enter username: ")
password = input("Enter password: ")
ftp.login(username, password)