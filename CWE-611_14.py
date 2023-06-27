#5.# CWE-611: Improper Input Validation
# Vulnerable line: line 9
# Description: This code does not properly validate user input, allowing for potential format string attacks.
import sys

input_str = input("Enter a string: ")

sys.stdout.write(input_str)