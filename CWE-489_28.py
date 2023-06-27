#9.# CWE-489: Use of a Function with Known Vulnerabilities
# This code uses a function with known vulnerabilities that can be exploited by attackers
# Vulnerable line: line 4
import base64

password = "password123"
encoded_password = base64.b64encode(password.encode())
print(encoded_password)