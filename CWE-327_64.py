#5.# Example 5: Use of subprocess module without proper input validation

import subprocess

user_input = input("Enter a command: ")
subprocess.call(user_input) # CWE-327: Use of subprocess module without proper input validation