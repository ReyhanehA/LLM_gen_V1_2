#4.# Path Traversal:


import os

filename = input("Enter filename: ")

with open(os.path.join('/home/user/files', filename), 'r') as f:
    contents = f.read()

# The vulnerable line is the os.path.join call that concatenates user input without proper sanitization, allowing for path traversal attacks.