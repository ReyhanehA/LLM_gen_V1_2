#3.# CWE-377: Insecure Temporary File Creation
# Vulnerable line: f = open('/var/tmp/myfile.txt', 'w')
# Description: This code creates a temporary file in a system-wide temporary directory, which can be accessed by other users on the system.
import os
f = open('/var/tmp/myfile.txt', 'w')
f.write('Hello, world!')
f.close()
os.remove('/var/tmp/myfile.txt')