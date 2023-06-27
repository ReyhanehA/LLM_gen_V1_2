#4.# Path Traversal:

# Vulnerable line:
file = open("/var/www/html/" + filename, "r")

# Description: This code is vulnerable to path traversal as it concatenates user input directly into a file path without proper sanitization.