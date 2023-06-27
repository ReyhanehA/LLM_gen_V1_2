#9.# CWE-611: Improper Input Validation
# Vulnerable line: line 3
# Description: This code does not validate user input before using it in a file path
import os

user_input = input("Enter a file name: ")
with open(user_input, 'w') as f:
    f.write("Hello, world!")