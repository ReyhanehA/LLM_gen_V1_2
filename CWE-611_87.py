#8.# CWE-611: Improper Input Validation
# Vulnerable line: line 11
# Description: This code takes user input without validating it, allowing for potential injection attacks.
import json
data = input("Enter some JSON data: ")
json_data = json.loads(data)
print(json_data)