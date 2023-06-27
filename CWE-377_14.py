#5.# CWE-377: Insecure Temporary File Creation
# Vulnerable line: f = open('tempfile.txt', 'w+')
# Description: This code creates a temporary file in the current working directory and allows other users on the system to read and write to it.
import os
f = open('tempfile.txt', 'w+')
f.write('Hello, world!')
f.seek(0)
print(f.read())
f.close()
os.remove('tempfile.txt')