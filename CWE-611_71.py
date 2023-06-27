#2.# CWE-611: Improper Input Validation
# Vulnerable line: line 7
# Description: This code takes user input without validating it, allowing for potential injection attacks.
import subprocess

command = input("Enter a command: ")
subprocess.call(command)