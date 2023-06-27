#8.# CWE-611: Improper Input Validation
# Vulnerable line: line 12
# Description: This code does not properly validate user input, allowing for potential command injection attacks.
import subprocess

filename = input("Enter a filename: ")

subprocess.call(["cat", filename])