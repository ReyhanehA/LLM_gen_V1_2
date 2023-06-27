#1.# CWE-611: Improper Input Validation
# Vulnerable line: line 4
# Description: This code takes user input without validating it, allowing for potential injection attacks.
user_input = input("Enter your name: ")
print("Hello, " + user_input + "!")