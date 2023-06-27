#3.# CWE-611: Improper Input Validation
# Vulnerable line: line 6
# Description: This code takes user input without validating it, allowing for potential injection attacks.
filename = input("Enter a filename: ")
with open(filename, "r") as file:
    print(file.read())