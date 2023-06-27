#4.# Example 4: Use of os.system() function without proper input validation

import os

user_input = input("Enter a command: ")
os.system(user_input) # CWE-327: Use of os.system() function without proper input validation