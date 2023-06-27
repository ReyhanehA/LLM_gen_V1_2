#6.# CWE-611: Improper Input Validation
# Vulnerable line: line 10
# Description: This code does not properly validate user input, allowing for potential integer overflow attacks.
import sys

input_int = int(input("Enter an integer: "))

sys.stdout.write(str(input_int))