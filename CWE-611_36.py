#7.# CWE-611: Improper Input Validation
# Vulnerable line: line 10
# Description: This code takes user input without validating it, allowing for potential injection attacks.
import requests
url = input("Enter a URL: ")
response = requests.get(url)
print(response.content)