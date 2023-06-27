#8.# CWE-547: Use of Untrusted Input for File Operations
filename = input("Enter the filename: ") # vulnerable line
with open(filename, "r") as f:
    print(f.read())
# This code uses untrusted user input (filename) for file operations, which can lead to various security vulnerabilities such as directory traversal.