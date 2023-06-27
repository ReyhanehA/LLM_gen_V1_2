#5.# CWE-377: Insecure Temporary File Creation
# Vulnerable line: f = open('tempfile.txt', 'a')
# Description: This code creates a temporary file in the current working directory which can be accessed by other users on the system.

f = open('tempfile.txt', 'a')