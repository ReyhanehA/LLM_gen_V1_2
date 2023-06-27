#8.# CWE-377: Insecure Temporary File Creation
# Vulnerable line: f = open('tempfile.txt', 'a')
# Description: This code creates a temporary file in the current working directory and allows other users on the system to append to it.
import os
f = open('tempfile.txt', 'a')
f.write('Hello, world!')
f.close()
os.remove('tempfile.txt')