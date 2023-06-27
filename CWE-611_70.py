#1.# CWE-611: Improper Input Validation
# Vulnerable line: line 5
# Description: This code takes user input without validating it, allowing for potential injection attacks.
import os

filename = input("Enter a filename: ")
os.system("rm " + filename)