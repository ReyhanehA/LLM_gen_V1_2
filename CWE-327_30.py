#1.# Example 1: CWE-327 - Use of a Broken or Risky Cryptographic Algorithm

import hashlib

password = "password123"
hash_object = hashlib.md5(password.encode())
print(hash_object.hexdigest()) # Vulnerable line: using MD5, a broken cryptographic algorithm