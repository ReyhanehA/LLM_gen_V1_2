#4.# Example 4: CWE-327 - Use of a Broken or Risky Cryptographic Algorithm

import random

password = "password123"
salt = str(random.randint(1000, 9999))
hash_object = hashlib.sha256((password + salt).encode())
print(hash_object.hexdigest()) # Vulnerable line: using a weak salt for password hashing