#2.# Example 2: CWE-327 - Use of a Broken or Risky Cryptographic Algorithm

import base64

password = "password123"
encoded_password = base64.b64encode(password.encode())
print(encoded_password) # Vulnerable line: using base64 encoding for password storage, which is not secure