#6.# CWE-377: Insecure Temporary File Creation
# Vulnerable line: f = open('/var/tmp/myfile.txt', 'w+')
# Description: This code creates a temporary file in a system-wide temporary directory and allows other users on the system to read and write to it.
import os
f = open('/var/tmp/myfile.txt', 'w+')
f.write('Hello, world!')
f.seek(0)
print(f.read())
f.close()
os.remove('/var/tmp/myfile.txt')