#8.# Improper Access Control:


import os

filename = input("Enter filename: ")

if os.path.exists(filename):
    with open(filename, 'r') as f:
        contents = f.read()
else:
    print("File not found.")

# The vulnerable line is the lack of proper access control, allowing users to access files they should not have access to.