#4.# CWE-489: Improper Input Validation
# Vulnerable line: line 7
# Description: This code takes user input without validating it, allowing for potential injection attacks.
import os
filename = input("Enter a filename: ")
os.remove(filename)