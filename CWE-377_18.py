#9.# CWE-377: Insecure Temporary File Creation
# Vulnerable line: f = open('/var/tmp/myfile.txt', 'a')
# Description: This code creates a temporary file in a system-wide temporary directory and allows other users on the system to append to it.
import os
f = open('/var/tmp/myfile.txt', 'a')
f.write('Hello, world!')
f.close()
os.remove('/var/tmp/myfile.txt')