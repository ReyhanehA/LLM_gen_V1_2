#1.# CWE-377: Insecure Temporary File Creation
# Vulnerable line: f = open('/tmp/myfile', 'w')
# Description: This code creates a temporary file in an insecure location (/tmp) which can be accessed by other users on the system.

f = open('/tmp/myfile', 'w')