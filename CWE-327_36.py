#7.# Example 7: CWE-327 - Use of a Broken or Risky Cryptographic Algorithm

import pyDes

message = "Hello, world!"
key = "secret_key"
des = pyDes.des(key, pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
encrypted_message = des.encrypt(message)
print(encrypted_message) # Vulnerable line: using DES with a weak key