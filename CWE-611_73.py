#4.# CWE-611: Improper Input Validation
# Vulnerable line: line 6
# Description: This code takes user input without validating it, allowing for potential injection attacks.
import urllib.request

url = input("Enter a URL: ")
urllib.request.urlopen(url)