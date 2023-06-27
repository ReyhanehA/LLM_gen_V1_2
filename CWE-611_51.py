#2.# CWE-611: Improper Input Validation
# Vulnerable line: line 6
# Description: This code does not properly validate user input, allowing for potential command injection attacks.
import os

filename = input("Enter a filename: ")

os.system("cat {}".format(filename))