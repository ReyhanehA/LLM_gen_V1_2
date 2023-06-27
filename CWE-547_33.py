#4.# CWE-547: Use of Unvalidated Input
username = input("Enter your username: ") # vulnerable line
# This code does not validate the user input, which can lead to various security vulnerabilities such as SQL injection.