#5.# CWE-611: Improper Input Validation
# Vulnerable line: line 3
# Description: This code takes user input without validating it, allowing for potential injection attacks.
import json

data = input("Enter JSON data: ")
json.loads(data)