#9.# Information Exposure:


import os

username = input("Enter username: ")

if os.path.exists(username + '.txt'):
    with open(username + '.txt', 'r') as f:
        contents = f.read()
else:
    print("User not found.")

# The vulnerable line is the error message that reveals whether a user exists or not, allowing for information exposure attacks.