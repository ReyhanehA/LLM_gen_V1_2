#6.# Example 6: CWE-327 - Use of a Broken or Risky Cryptographic Algorithm

import rsa

message = "Hello, world!"
(public_key, private_key) = rsa.newkeys(512)
encrypted_message = rsa.encrypt(message.encode(), public_key)
print(encrypted_message) # Vulnerable line: using RSA with a weak key size