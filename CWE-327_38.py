#9.# Example 9: CWE-327 - Use of a Broken or Risky Cryptographic Algorithm

import hashlib

password = "password123"
hash_object = hashlib.sha1(password.encode())
print(hash_object.hexdigest()) # Vulnerable line: using SHA-1, a broken cryptographic algorithm