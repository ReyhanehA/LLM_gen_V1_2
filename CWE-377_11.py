#2.# CWE-377: Insecure Temporary File Creation
# Vulnerable line: f = open('tempfile.txt', 'w')
# Description: This code creates a temporary file in the current working directory, which can be accessed by other users on the system.
import os
f = open('tempfile.txt', 'w')
f.write('Hello, world!')
f.close()
os.remove('tempfile.txt')