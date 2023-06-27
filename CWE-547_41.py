#2.# Command Injection:


import os

command = input("Enter command: ")

os.system("ping " + command)

# The vulnerable line is the os.system call that concatenates user input without proper sanitization, allowing for command injection attacks.