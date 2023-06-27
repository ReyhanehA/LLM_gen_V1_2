#2.# CWE-489: Improper Input Validation
# Vulnerable line: line 5
# Description: This code takes user input without validating it, allowing for potential injection attacks.
password = input("Enter your password: ")
if password == "admin":
    print("Access granted!")
else:
    print("Access denied.")