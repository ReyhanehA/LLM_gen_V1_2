#7.# CWE-377: Insecure Temporary File Creation
# Vulnerable line: f = open('/tmp/myfile.txt', 'a')
# Description: This code creates a temporary file in an insecure location and allows other users on the system to append to it.
import os
f = open('/tmp/myfile.txt', 'a')
f.write('Hello, world!')
f.close()
os.remove('/tmp/myfile.txt')