#10.# CWE-377: Insecure Temporary File Creation
# Vulnerable line: f = open('/tmp/myfile.txt', 'wb')
# Description: This code creates a temporary file in an insecure location and allows other users on the system to write binary data to it.
import os
f = open('/tmp/myfile.txt', 'wb')
f.write(b'\x48\x65\x6c\x6c\x6f\x2c\x20\x77\x6f\x72\x6c\x64\x21')
f.close()
os.remove('/tmp/myfile.txt')