#6.# CWE-611: Improper Input Validation
# Vulnerable line: line 3
# Description: This code does not validate user input before using it in a file path
import os

user_input = input("Enter a file name: ")
os.remove(user_input)