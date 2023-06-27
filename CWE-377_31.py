#2.# CWE-377: Insecure Temporary File Creation

import os

# Vulnerable line: creating a temporary file without setting secure permissions
temp_file = open(os.tmpfile(), 'w')