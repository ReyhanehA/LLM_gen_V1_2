#5.# CWE-611: Improper Input Validation
# Vulnerable line: line 4
# Description: This code does not validate user input before using it in a system command
import os

user_input = input("Enter a file name: ")
os.system("cat {}".format(user_input))